# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=unused-argument

from knack.log import get_logger

from ..utils import get_arc_autonomous_cloud_fqdn, is_arc_autonomous_cloud
from .DefaultExtension import DefaultExtension

logger = get_logger(__name__)


class PrometheusCollector(DefaultExtension):
    def Create(self, cmd, client, resource_group_name, cluster_name, name, cluster_type, cluster_rp,
               extension_type, scope, auto_upgrade_minor_version, release_train, version, target_namespace,
               release_namespace, configuration_settings, configuration_protected_settings,
               configuration_settings_file, configuration_protected_settings_file,
               plan_name, plan_publisher, plan_product):
        # Override extension name, release-namespace and scope.
        name = 'azuremonitor-metrics'
        release_namespace = 'kube-system'
        scope = 'cluster'

        logger.warning('Ignoring name, release-namespace and scope parameters since %s '
                       'only supports cluster scope and single instance of this extension.', extension_type)
        logger.warning("Defaulting to extension name '%s' and release-namespace '%s'", name, release_namespace)

        if is_arc_autonomous_cloud(configuration_settings):
            logger.info('Overriding the FQDN configuration automatically for Winfield')
            configuration_settings['Azure.proxySettings.autonomousFqdn'] = get_arc_autonomous_cloud_fqdn(cmd)

        return DefaultExtension.Create(self, cmd, client, resource_group_name, cluster_name, name, cluster_type, cluster_rp,
                                       extension_type, scope, auto_upgrade_minor_version, release_train, version, target_namespace,
                                       release_namespace, configuration_settings, configuration_protected_settings,
                                       configuration_settings_file, configuration_protected_settings_file,
                                       plan_name, plan_publisher, plan_product)
