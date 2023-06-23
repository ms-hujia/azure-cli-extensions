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
    "networkcloud defaultcninetwork show",
    is_experimental=True,
)
class Show(AAZCommand):
    """Get properties of the provided default CNI network.

    :example: Get default CNI network
        az networkcloud defaultcninetwork show --name "defaultCniNetworkName" --resource-group "resourceGroupName"
    """

    _aaz_info = {
        "version": "2022-12-12-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.networkcloud/defaultcninetworks/{}", "2022-12-12-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.default_cni_network_name = AAZStrArg(
            options=["-n", "--name", "--default-cni-network-name"],
            help="The name of the default CNI network.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^([a-zA-Z0-9][a-zA-Z0-9-_]{0,28}[a-zA-Z0-9])$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.DefaultCniNetworksGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class DefaultCniNetworksGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/defaultCniNetworks/{defaultCniNetworkName}",
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
                    "defaultCniNetworkName", self.ctx.args.default_cni_network_name,
                    required=True,
                ),
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
                    "api-version", "2022-12-12-preview",
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
            _schema_on_200.extended_location = AAZObjectType(
                serialized_name="extendedLocation",
                flags={"required": True},
            )
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            extended_location = cls._schema_on_200.extended_location
            extended_location.name = AAZStrType(
                flags={"required": True},
            )
            extended_location.type = AAZStrType(
                flags={"required": True},
            )

            properties = cls._schema_on_200.properties
            properties.cluster_id = AAZStrType(
                serialized_name="clusterId",
                flags={"read_only": True},
            )
            properties.cni_as_number = AAZIntType(
                serialized_name="cniAsNumber",
                flags={"read_only": True},
            )
            properties.cni_bgp_configuration = AAZObjectType(
                serialized_name="cniBgpConfiguration",
            )
            properties.detailed_status = AAZStrType(
                serialized_name="detailedStatus",
                flags={"read_only": True},
            )
            properties.detailed_status_message = AAZStrType(
                serialized_name="detailedStatusMessage",
                flags={"read_only": True},
            )
            properties.fabric_bgp_peers = AAZListType(
                serialized_name="fabricBgpPeers",
                flags={"read_only": True},
            )
            properties.hybrid_aks_clusters_associated_ids = AAZListType(
                serialized_name="hybridAksClustersAssociatedIds",
                flags={"read_only": True},
            )
            properties.interface_name = AAZStrType(
                serialized_name="interfaceName",
                flags={"read_only": True},
            )
            properties.ip_allocation_type = AAZStrType(
                serialized_name="ipAllocationType",
            )
            properties.ipv4_connected_prefix = AAZStrType(
                serialized_name="ipv4ConnectedPrefix",
            )
            properties.ipv6_connected_prefix = AAZStrType(
                serialized_name="ipv6ConnectedPrefix",
            )
            properties.l3_isolation_domain_id = AAZStrType(
                serialized_name="l3IsolationDomainId",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.vlan = AAZIntType(
                flags={"required": True},
            )

            cni_bgp_configuration = cls._schema_on_200.properties.cni_bgp_configuration
            cni_bgp_configuration.bgp_peers = AAZListType(
                serialized_name="bgpPeers",
            )
            cni_bgp_configuration.community_advertisements = AAZListType(
                serialized_name="communityAdvertisements",
            )
            cni_bgp_configuration.service_external_prefixes = AAZListType(
                serialized_name="serviceExternalPrefixes",
            )
            cni_bgp_configuration.service_load_balancer_prefixes = AAZListType(
                serialized_name="serviceLoadBalancerPrefixes",
            )

            bgp_peers = cls._schema_on_200.properties.cni_bgp_configuration.bgp_peers
            bgp_peers.Element = AAZObjectType()
            _ShowHelper._build_schema_bgp_peer_read(bgp_peers.Element)

            community_advertisements = cls._schema_on_200.properties.cni_bgp_configuration.community_advertisements
            community_advertisements.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.cni_bgp_configuration.community_advertisements.Element
            _element.communities = AAZListType(
                flags={"required": True},
            )
            _element.subnet_prefix = AAZStrType(
                serialized_name="subnetPrefix",
                flags={"required": True},
            )

            communities = cls._schema_on_200.properties.cni_bgp_configuration.community_advertisements.Element.communities
            communities.Element = AAZStrType()

            service_external_prefixes = cls._schema_on_200.properties.cni_bgp_configuration.service_external_prefixes
            service_external_prefixes.Element = AAZStrType()

            service_load_balancer_prefixes = cls._schema_on_200.properties.cni_bgp_configuration.service_load_balancer_prefixes
            service_load_balancer_prefixes.Element = AAZStrType()

            fabric_bgp_peers = cls._schema_on_200.properties.fabric_bgp_peers
            fabric_bgp_peers.Element = AAZObjectType()
            _ShowHelper._build_schema_bgp_peer_read(fabric_bgp_peers.Element)

            hybrid_aks_clusters_associated_ids = cls._schema_on_200.properties.hybrid_aks_clusters_associated_ids
            hybrid_aks_clusters_associated_ids.Element = AAZStrType()

            system_data = cls._schema_on_200.system_data
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

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _ShowHelper:
    """Helper class for Show"""

    _schema_bgp_peer_read = None

    @classmethod
    def _build_schema_bgp_peer_read(cls, _schema):
        if cls._schema_bgp_peer_read is not None:
            _schema.as_number = cls._schema_bgp_peer_read.as_number
            _schema.peer_ip = cls._schema_bgp_peer_read.peer_ip
            return

        cls._schema_bgp_peer_read = _schema_bgp_peer_read = AAZObjectType()

        bgp_peer_read = _schema_bgp_peer_read
        bgp_peer_read.as_number = AAZIntType(
            serialized_name="asNumber",
            flags={"required": True},
        )
        bgp_peer_read.peer_ip = AAZStrType(
            serialized_name="peerIp",
            flags={"required": True},
        )

        _schema.as_number = cls._schema_bgp_peer_read.as_number
        _schema.peer_ip = cls._schema_bgp_peer_read.peer_ip


__all__ = ["Show"]
