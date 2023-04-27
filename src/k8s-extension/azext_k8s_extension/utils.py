# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import json
from typing import Tuple
from urllib.parse import urlparse
from . import consts
from azure.cli.core.azclierror import AzureResponseError, InvalidArgumentValueError, RequiredArgumentMissingError


def get_cluster_rp_api_version(cluster_type, cluster_rp=None) -> Tuple[str, str]:
    if cluster_type.lower() == consts.PROVISIONED_CLUSTER_TYPE:
        if cluster_rp is None or cluster_rp.strip() == "":
            raise RequiredArgumentMissingError(
                "Error! Cluster Resource Provider value is required for Cluster Type '{}'".format(cluster_type)
            )
        if cluster_rp.lower() == consts.HYBRIDCONTAINERSERVICE_RP:
            return (
                consts.HYBRIDCONTAINERSERVICE_RP,
                consts.HYBRIDCONTAINERSERVICE_API_VERSION,
            )
        raise InvalidArgumentValueError(
            "Error! Cluster type '{}' and Cluster Resource Provider '{}' combination is not supported".format(cluster_type, cluster_rp)
        )
    if cluster_type.lower() == consts.CONNECTED_CLUSTER_TYPE:
        return consts.CONNECTED_CLUSTER_RP, consts.CONNECTED_CLUSTER_API_VERSION
    if cluster_type.lower() == consts.APPLIANCE_TYPE:
        return consts.APPLIANCE_RP, consts.APPLIANCE_API_VERSION
    if (
        cluster_type.lower() == ""
        or cluster_type.lower() == consts.MANAGED_CLUSTER_TYPE
    ):
        return consts.MANAGED_CLUSTER_RP, consts.MANAGED_CLUSTER_API_VERSION
    raise InvalidArgumentValueError(
        "Error! Cluster type '{}' is not supported".format(cluster_type)
    )


def read_config_settings_file(file_path):
    try:
        with open(file_path, "r") as f:
            settings = json.load(f)
            if len(settings) == 0:
                raise Exception("File {} is empty".format(file_path))
            return settings
    except ValueError as ex:
        raise Exception("File {} is not a valid JSON file".format(file_path)) from ex


def is_dogfood_cluster(cmd):
    return (
        urlparse(cmd.cli_ctx.cloud.endpoints.resource_manager).hostname
        == consts.DF_RM_HOSTNAME
    )


def is_arc_autonomous_cloud(configuration_settings):
    # Determine if the cloud is Arc Autonomous by checking a configuration setting named isArcAutonomous.
    is_arc_autonomous = False

    if 'isArcAutonomous' in configuration_settings:
        is_arc_autonomous_setting = configuration_settings['isArcAutonomous']
        if (isinstance(is_arc_autonomous_setting, str) and str(is_arc_autonomous_setting).lower() == "true") or (isinstance(is_arc_autonomous_setting, bool) and is_arc_autonomous_setting):
            is_arc_autonomous = True
            del configuration_settings['isArcAutonomous']

    return is_arc_autonomous


def get_arc_autonomou_cloud_fqdn(cmd):
    # Get the Arc Autonomous FQDN.
    metadata = get_metadata(cmd.cli_ctx.cloud.endpoints.resource_manager, "2022-09-01")

    return metadata['suffixes']['storage']


def get_metadata(arm_endpoint, api_version="2015-01-01"):
    metadata_url_suffix = f"/metadata/endpoints?api-version={api_version}"
    try:
        error_msg_fmt = "Unable to get metadata endpoints from the cloud.\n{}"
        import requests
        session = requests.Session()
        metadata_endpoint = arm_endpoint + metadata_url_suffix
        response = session.get(metadata_endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            msg = "Server returned status code {} for {}".format(response.status_code, metadata_endpoint)
            raise AzureResponseError(error_msg_fmt.format(msg))
    except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as err:
        msg = "Please ensure you have network connection. Error detail: {}".format(str(err))
        raise AzureResponseError(error_msg_fmt.format(msg))
    except ValueError as err:
        msg = "Response body does not contain valid json. Error detail: {}".format(str(err))
        raise AzureResponseError(error_msg_fmt.format(msg))
