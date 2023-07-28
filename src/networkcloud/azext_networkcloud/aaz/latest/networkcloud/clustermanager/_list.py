# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "networkcloud clustermanager list",
    is_preview=True,
)
class List(AAZCommand):
    """List cluster managers in the provided resource group or subscription.

    :example: List cluster managers for subscription
        az networkcloud clustermanager list

    :example: List cluster managers for resource group
        az networkcloud clustermanager list --resource-group "resourceGroupName"
    """

    _aaz_info = {
        "version": "2023-07-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.networkcloud/clustermanagers", "2023-07-01"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.networkcloud/clustermanagers", "2023-07-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_paging(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        condition_1 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        if condition_0:
            self.ClusterManagersListByResourceGroup(ctx=self.ctx)()
        if condition_1:
            self.ClusterManagersListBySubscription(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance.value, client_flatten=True)
        next_link = self.deserialize_output(self.ctx.vars.instance.next_link)
        return result, next_link

    class ClusterManagersListByResourceGroup(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/clusterManagers",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-07-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.analytics_workspace_id = AAZStrType(
                serialized_name="analyticsWorkspaceId",
            )
            properties.availability_zones = AAZListType(
                serialized_name="availabilityZones",
            )
            properties.cluster_versions = AAZListType(
                serialized_name="clusterVersions",
                flags={"read_only": True},
            )
            properties.detailed_status = AAZStrType(
                serialized_name="detailedStatus",
                flags={"read_only": True},
            )
            properties.detailed_status_message = AAZStrType(
                serialized_name="detailedStatusMessage",
                flags={"read_only": True},
            )
            properties.fabric_controller_id = AAZStrType(
                serialized_name="fabricControllerId",
                flags={"required": True},
            )
            properties.managed_resource_group_configuration = AAZObjectType(
                serialized_name="managedResourceGroupConfiguration",
            )
            properties.manager_extended_location = AAZObjectType(
                serialized_name="managerExtendedLocation",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.vm_size = AAZStrType(
                serialized_name="vmSize",
            )

            availability_zones = cls._schema_on_200.value.Element.properties.availability_zones
            availability_zones.Element = AAZStrType()

            cluster_versions = cls._schema_on_200.value.Element.properties.cluster_versions
            cluster_versions.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.cluster_versions.Element
            _element.support_expiry_date = AAZStrType(
                serialized_name="supportExpiryDate",
                flags={"read_only": True},
            )
            _element.target_cluster_version = AAZStrType(
                serialized_name="targetClusterVersion",
                flags={"read_only": True},
            )

            managed_resource_group_configuration = cls._schema_on_200.value.Element.properties.managed_resource_group_configuration
            managed_resource_group_configuration.location = AAZStrType()
            managed_resource_group_configuration.name = AAZStrType()

            manager_extended_location = cls._schema_on_200.value.Element.properties.manager_extended_location
            manager_extended_location.name = AAZStrType(
                flags={"required": True},
            )
            manager_extended_location.type = AAZStrType(
                flags={"required": True},
            )

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200

    class ClusterManagersListBySubscription(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/providers/Microsoft.NetworkCloud/clusterManagers",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-07-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.next_link = AAZStrType(
                serialized_name="nextLink",
            )
            _schema_on_200.value = AAZListType()

            value = cls._schema_on_200.value
            value.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element
            _element.id = AAZStrType(
                flags={"read_only": True},
            )
            _element.location = AAZStrType(
                flags={"required": True},
            )
            _element.name = AAZStrType(
                flags={"read_only": True},
            )
            _element.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _element.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _element.tags = AAZDictType()
            _element.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.value.Element.properties
            properties.analytics_workspace_id = AAZStrType(
                serialized_name="analyticsWorkspaceId",
            )
            properties.availability_zones = AAZListType(
                serialized_name="availabilityZones",
            )
            properties.cluster_versions = AAZListType(
                serialized_name="clusterVersions",
                flags={"read_only": True},
            )
            properties.detailed_status = AAZStrType(
                serialized_name="detailedStatus",
                flags={"read_only": True},
            )
            properties.detailed_status_message = AAZStrType(
                serialized_name="detailedStatusMessage",
                flags={"read_only": True},
            )
            properties.fabric_controller_id = AAZStrType(
                serialized_name="fabricControllerId",
                flags={"required": True},
            )
            properties.managed_resource_group_configuration = AAZObjectType(
                serialized_name="managedResourceGroupConfiguration",
            )
            properties.manager_extended_location = AAZObjectType(
                serialized_name="managerExtendedLocation",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.vm_size = AAZStrType(
                serialized_name="vmSize",
            )

            availability_zones = cls._schema_on_200.value.Element.properties.availability_zones
            availability_zones.Element = AAZStrType()

            cluster_versions = cls._schema_on_200.value.Element.properties.cluster_versions
            cluster_versions.Element = AAZObjectType()

            _element = cls._schema_on_200.value.Element.properties.cluster_versions.Element
            _element.support_expiry_date = AAZStrType(
                serialized_name="supportExpiryDate",
                flags={"read_only": True},
            )
            _element.target_cluster_version = AAZStrType(
                serialized_name="targetClusterVersion",
                flags={"read_only": True},
            )

            managed_resource_group_configuration = cls._schema_on_200.value.Element.properties.managed_resource_group_configuration
            managed_resource_group_configuration.location = AAZStrType()
            managed_resource_group_configuration.name = AAZStrType()

            manager_extended_location = cls._schema_on_200.value.Element.properties.manager_extended_location
            manager_extended_location.name = AAZStrType(
                flags={"required": True},
            )
            manager_extended_location.type = AAZStrType(
                flags={"required": True},
            )

            system_data = cls._schema_on_200.value.Element.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.value.Element.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ListHelper:
    """Helper class for List"""


__all__ = ["List"]
