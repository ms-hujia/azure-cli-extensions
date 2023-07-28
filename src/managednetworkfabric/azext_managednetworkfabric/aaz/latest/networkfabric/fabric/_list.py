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
    "networkfabric fabric list",
)
class List(AAZCommand):
    """List all Network Fabrics in the provided resource group or subscription.

    :example: List the Network Fabrics for Resource Group
        az networkfabric fabric list --resource-group "example-rg"

    :example: List the Network Fabrics for Subscription
        az networkfabric fabric list --subscription "<subscriptionId>"
    """

    _aaz_info = {
        "version": "2023-02-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.managednetworkfabric/networkfabrics", "2023-02-01-preview"],
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/networkfabrics", "2023-02-01-preview"],
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
        _args_schema.resource_group = AAZResourceGroupNameArg(
            help="Name of the resource group",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        condition_0 = has_value(self.ctx.args.resource_group) and has_value(self.ctx.subscription_id)
        condition_1 = has_value(self.ctx.subscription_id) and has_value(self.ctx.args.resource_group) is not True
        if condition_0:
            self.NetworkFabricsListByResourceGroup(ctx=self.ctx)()
        if condition_1:
            self.NetworkFabricsListBySubscription(ctx=self.ctx)()
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

    class NetworkFabricsListByResourceGroup(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/networkFabrics",
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
                    "api-version", "2023-02-01-preview",
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
                flags={"client_flatten": True},
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
            properties.annotation = AAZStrType()
            properties.fabric_asn = AAZIntType(
                serialized_name="fabricASN",
                flags={"required": True},
            )
            properties.ipv4_prefix = AAZStrType(
                serialized_name="ipv4Prefix",
            )
            properties.ipv6_prefix = AAZStrType(
                serialized_name="ipv6Prefix",
            )
            properties.l2_isolation_domains = AAZListType(
                serialized_name="l2IsolationDomains",
                flags={"read_only": True},
            )
            properties.l3_isolation_domains = AAZListType(
                serialized_name="l3IsolationDomains",
                flags={"read_only": True},
            )
            properties.management_network_configuration = AAZObjectType(
                serialized_name="managementNetworkConfiguration",
                flags={"required": True},
            )
            properties.network_fabric_controller_id = AAZStrType(
                serialized_name="networkFabricControllerId",
                flags={"required": True},
            )
            properties.network_fabric_sku = AAZStrType(
                serialized_name="networkFabricSku",
                flags={"required": True},
            )
            properties.operational_state = AAZStrType(
                serialized_name="operationalState",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rack_count = AAZIntType(
                serialized_name="rackCount",
                flags={"required": True},
            )
            properties.racks = AAZListType(
                flags={"read_only": True},
            )
            properties.router_id = AAZStrType(
                serialized_name="routerId",
                flags={"read_only": True},
            )
            properties.server_count_per_rack = AAZIntType(
                serialized_name="serverCountPerRack",
                flags={"required": True},
            )
            properties.terminal_server_configuration = AAZObjectType(
                serialized_name="terminalServerConfiguration",
                flags={"required": True},
            )

            l2_isolation_domains = cls._schema_on_200.value.Element.properties.l2_isolation_domains
            l2_isolation_domains.Element = AAZStrType()

            l3_isolation_domains = cls._schema_on_200.value.Element.properties.l3_isolation_domains
            l3_isolation_domains.Element = AAZStrType()

            management_network_configuration = cls._schema_on_200.value.Element.properties.management_network_configuration
            management_network_configuration.infrastructure_vpn_configuration = AAZObjectType(
                serialized_name="infrastructureVpnConfiguration",
                flags={"required": True},
            )
            _ListHelper._build_schema_vpn_configuration_properties_read(management_network_configuration.infrastructure_vpn_configuration)
            management_network_configuration.workload_vpn_configuration = AAZObjectType(
                serialized_name="workloadVpnConfiguration",
                flags={"required": True},
            )
            _ListHelper._build_schema_vpn_configuration_properties_read(management_network_configuration.workload_vpn_configuration)

            racks = cls._schema_on_200.value.Element.properties.racks
            racks.Element = AAZStrType()

            terminal_server_configuration = cls._schema_on_200.value.Element.properties.terminal_server_configuration
            terminal_server_configuration.network_device_id = AAZStrType(
                serialized_name="networkDeviceId",
                flags={"read_only": True},
            )
            terminal_server_configuration.password = AAZStrType(
                flags={"required": True, "secret": True},
            )
            terminal_server_configuration.primary_ipv4_prefix = AAZStrType(
                serialized_name="primaryIpv4Prefix",
                flags={"required": True},
            )
            terminal_server_configuration.primary_ipv6_prefix = AAZStrType(
                serialized_name="primaryIpv6Prefix",
            )
            terminal_server_configuration.secondary_ipv4_prefix = AAZStrType(
                serialized_name="secondaryIpv4Prefix",
                flags={"required": True},
            )
            terminal_server_configuration.secondary_ipv6_prefix = AAZStrType(
                serialized_name="secondaryIpv6Prefix",
            )
            terminal_server_configuration.serial_number = AAZStrType(
                serialized_name="serialNumber",
            )
            terminal_server_configuration.username = AAZStrType(
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

    class NetworkFabricsListBySubscription(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/providers/Microsoft.ManagedNetworkFabric/networkFabrics",
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
                    "api-version", "2023-02-01-preview",
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
                flags={"client_flatten": True},
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
            properties.annotation = AAZStrType()
            properties.fabric_asn = AAZIntType(
                serialized_name="fabricASN",
                flags={"required": True},
            )
            properties.ipv4_prefix = AAZStrType(
                serialized_name="ipv4Prefix",
            )
            properties.ipv6_prefix = AAZStrType(
                serialized_name="ipv6Prefix",
            )
            properties.l2_isolation_domains = AAZListType(
                serialized_name="l2IsolationDomains",
                flags={"read_only": True},
            )
            properties.l3_isolation_domains = AAZListType(
                serialized_name="l3IsolationDomains",
                flags={"read_only": True},
            )
            properties.management_network_configuration = AAZObjectType(
                serialized_name="managementNetworkConfiguration",
                flags={"required": True},
            )
            properties.network_fabric_controller_id = AAZStrType(
                serialized_name="networkFabricControllerId",
                flags={"required": True},
            )
            properties.network_fabric_sku = AAZStrType(
                serialized_name="networkFabricSku",
                flags={"required": True},
            )
            properties.operational_state = AAZStrType(
                serialized_name="operationalState",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rack_count = AAZIntType(
                serialized_name="rackCount",
                flags={"required": True},
            )
            properties.racks = AAZListType(
                flags={"read_only": True},
            )
            properties.router_id = AAZStrType(
                serialized_name="routerId",
                flags={"read_only": True},
            )
            properties.server_count_per_rack = AAZIntType(
                serialized_name="serverCountPerRack",
                flags={"required": True},
            )
            properties.terminal_server_configuration = AAZObjectType(
                serialized_name="terminalServerConfiguration",
                flags={"required": True},
            )

            l2_isolation_domains = cls._schema_on_200.value.Element.properties.l2_isolation_domains
            l2_isolation_domains.Element = AAZStrType()

            l3_isolation_domains = cls._schema_on_200.value.Element.properties.l3_isolation_domains
            l3_isolation_domains.Element = AAZStrType()

            management_network_configuration = cls._schema_on_200.value.Element.properties.management_network_configuration
            management_network_configuration.infrastructure_vpn_configuration = AAZObjectType(
                serialized_name="infrastructureVpnConfiguration",
                flags={"required": True},
            )
            _ListHelper._build_schema_vpn_configuration_properties_read(management_network_configuration.infrastructure_vpn_configuration)
            management_network_configuration.workload_vpn_configuration = AAZObjectType(
                serialized_name="workloadVpnConfiguration",
                flags={"required": True},
            )
            _ListHelper._build_schema_vpn_configuration_properties_read(management_network_configuration.workload_vpn_configuration)

            racks = cls._schema_on_200.value.Element.properties.racks
            racks.Element = AAZStrType()

            terminal_server_configuration = cls._schema_on_200.value.Element.properties.terminal_server_configuration
            terminal_server_configuration.network_device_id = AAZStrType(
                serialized_name="networkDeviceId",
                flags={"read_only": True},
            )
            terminal_server_configuration.password = AAZStrType(
                flags={"required": True, "secret": True},
            )
            terminal_server_configuration.primary_ipv4_prefix = AAZStrType(
                serialized_name="primaryIpv4Prefix",
                flags={"required": True},
            )
            terminal_server_configuration.primary_ipv6_prefix = AAZStrType(
                serialized_name="primaryIpv6Prefix",
            )
            terminal_server_configuration.secondary_ipv4_prefix = AAZStrType(
                serialized_name="secondaryIpv4Prefix",
                flags={"required": True},
            )
            terminal_server_configuration.secondary_ipv6_prefix = AAZStrType(
                serialized_name="secondaryIpv6Prefix",
            )
            terminal_server_configuration.serial_number = AAZStrType(
                serialized_name="serialNumber",
            )
            terminal_server_configuration.username = AAZStrType(
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

    _schema_vpn_configuration_properties_read = None

    @classmethod
    def _build_schema_vpn_configuration_properties_read(cls, _schema):
        if cls._schema_vpn_configuration_properties_read is not None:
            _schema.administrative_state = cls._schema_vpn_configuration_properties_read.administrative_state
            _schema.network_to_network_interconnect_id = cls._schema_vpn_configuration_properties_read.network_to_network_interconnect_id
            _schema.option_a_properties = cls._schema_vpn_configuration_properties_read.option_a_properties
            _schema.option_b_properties = cls._schema_vpn_configuration_properties_read.option_b_properties
            _schema.peering_option = cls._schema_vpn_configuration_properties_read.peering_option
            return

        cls._schema_vpn_configuration_properties_read = _schema_vpn_configuration_properties_read = AAZObjectType()

        vpn_configuration_properties_read = _schema_vpn_configuration_properties_read
        vpn_configuration_properties_read.administrative_state = AAZStrType(
            serialized_name="administrativeState",
            flags={"read_only": True},
        )
        vpn_configuration_properties_read.network_to_network_interconnect_id = AAZStrType(
            serialized_name="networkToNetworkInterconnectId",
            flags={"read_only": True},
        )
        vpn_configuration_properties_read.option_a_properties = AAZObjectType(
            serialized_name="optionAProperties",
        )
        vpn_configuration_properties_read.option_b_properties = AAZObjectType(
            serialized_name="optionBProperties",
        )
        vpn_configuration_properties_read.peering_option = AAZStrType(
            serialized_name="peeringOption",
            flags={"required": True},
        )

        option_a_properties = _schema_vpn_configuration_properties_read.option_a_properties
        option_a_properties.bfd_configuration = AAZObjectType(
            serialized_name="bfdConfiguration",
        )
        option_a_properties.mtu = AAZIntType()
        option_a_properties.peer_asn = AAZIntType(
            serialized_name="peerASN",
        )
        option_a_properties.primary_ipv4_prefix = AAZStrType(
            serialized_name="primaryIpv4Prefix",
        )
        option_a_properties.primary_ipv6_prefix = AAZStrType(
            serialized_name="primaryIpv6Prefix",
        )
        option_a_properties.secondary_ipv4_prefix = AAZStrType(
            serialized_name="secondaryIpv4Prefix",
        )
        option_a_properties.secondary_ipv6_prefix = AAZStrType(
            serialized_name="secondaryIpv6Prefix",
        )
        option_a_properties.vlan_id = AAZIntType(
            serialized_name="vlanId",
        )

        bfd_configuration = _schema_vpn_configuration_properties_read.option_a_properties.bfd_configuration
        bfd_configuration.interval = AAZIntType(
            flags={"read_only": True},
        )
        bfd_configuration.multiplier = AAZIntType(
            flags={"read_only": True},
        )

        option_b_properties = _schema_vpn_configuration_properties_read.option_b_properties
        option_b_properties.export_route_targets = AAZListType(
            serialized_name="exportRouteTargets",
            flags={"required": True},
        )
        option_b_properties.import_route_targets = AAZListType(
            serialized_name="importRouteTargets",
            flags={"required": True},
        )

        export_route_targets = _schema_vpn_configuration_properties_read.option_b_properties.export_route_targets
        export_route_targets.Element = AAZStrType()

        import_route_targets = _schema_vpn_configuration_properties_read.option_b_properties.import_route_targets
        import_route_targets.Element = AAZStrType()

        _schema.administrative_state = cls._schema_vpn_configuration_properties_read.administrative_state
        _schema.network_to_network_interconnect_id = cls._schema_vpn_configuration_properties_read.network_to_network_interconnect_id
        _schema.option_a_properties = cls._schema_vpn_configuration_properties_read.option_a_properties
        _schema.option_b_properties = cls._schema_vpn_configuration_properties_read.option_b_properties
        _schema.peering_option = cls._schema_vpn_configuration_properties_read.peering_option


__all__ = ["List"]
