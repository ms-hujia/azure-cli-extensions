# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=unused-argument

from urllib.parse import urlparse
from azure.cli.command_modules.role._client_factory import \
    _graph_client_factory
from azure.cli.command_modules.role._msgrpah._graph_objects import \
    set_object_properties
from knack.log import get_logger
from knack.util import CLIError

from ..utils import get_metadata, is_arc_autonomous_cloud
from .DefaultExtension import DefaultExtension, user_confirmation_factory

logger = get_logger(__name__)


class Grafana(DefaultExtension):
    def Create(self, cmd, client, resource_group_name, cluster_name, name, cluster_type, cluster_rp,
               extension_type, scope, auto_upgrade_minor_version, release_train, version, target_namespace,
               release_namespace, configuration_settings, configuration_protected_settings,
               configuration_settings_file, configuration_protected_settings_file,
               plan_name, plan_publisher, plan_product):
        # Check whether cloud is Arc Autonomous.
        if not is_arc_autonomous_cloud(configuration_settings):
            raise CLIError("Grafana extension is only available in Winfield")

        # Override extension name, release-namespace and scope.
        name = 'azuremonitor-grafana'
        release_namespace = 'grafana'
        scope = 'cluster'

        logger.warning('Ignoring name, release-namespace and scope parameters since %s '
                       'only supports cluster scope and single instance of this extension.', extension_type)
        logger.warning("Defaulting to extension name '%s' and release-namespace '%s'", name, release_namespace)

        # Create extra resources.
        logger.info("Creating extra resources for '%s'", extension_type)

        graph_client = _graph_client_factory(cmd.cli_ctx)

        body = {}

        set_object_properties('application', body,
                              enable_id_token_issuance=True,
                              )

        app = graph_client.application_create(body)

        logger.info(app)

        app_id = app['appId']

        body = {
            "appId": app_id,
            "accountEnabled": True
        }

        sp = graph_client.service_principal_create(body)

        logger.info(sp)

        # Override the configuration setting including FQDN and AAD application ID.
        logger.info('Overriding the FQDN configuration automatically for Winfield')

        metadata = get_metadata(cmd.cli_ctx.cloud.endpoints.resource_manager, "2022-09-01")

        configuration_settings['Grafana.AutonomousFqdn'] = metadata['suffixes']['storage']

        configuration_settings['Grafana.AzureArmUrl'] = cmd.cli_ctx.cloud.endpoints.resource_manager
        configuration_settings['Grafana.AzureArmScope'] = cmd.cli_ctx.cloud.endpoints.resource_manager
        configuration_settings['Grafana.AzureGraphUrl'] = metadata['graph']
        configuration_settings['Grafana.AzureGraphScope'] = metadata['graphAudience']
        configuration_settings['Grafana.StsHost'] = urlparse(metadata['authentication']['loginEndpoint']).hostname

        configuration_settings['Grafana.GrafanaAppId'] = app_id

        return DefaultExtension.Create(self, cmd, client, resource_group_name, cluster_name, name, cluster_type, cluster_rp,
                                       extension_type, scope, auto_upgrade_minor_version, release_train, version, target_namespace,
                                       release_namespace, configuration_settings, configuration_protected_settings,
                                       configuration_settings_file, configuration_protected_settings_file,
                                       plan_name, plan_publisher, plan_product)

    def Delete(
        self, cmd, client, resource_group_name, cluster_name, name, cluster_type, cluster_rp, yes
    ):
        # Get user confirmation.
        user_confirmation_factory(cmd, yes)

        # Delete the AAD application created for the extension.
        extension = client.get(
            resource_group_name, cluster_rp, cluster_type, cluster_name, name
        )

        app_id = extension.configuration_settings['Grafana.GrafanaAppId']

        graph_client = _graph_client_factory(cmd.cli_ctx)

        app = graph_client.application_list(filter="appId eq '{}'".format(app_id))

        if app:
            graph_client.application_delete(app[0]['id'])
        else:
            logger.warning("The AAD application %s is not found", app_id)
