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
    "networkcloud virtualmachine update",
    is_experimental=True,
)
class Update(AAZCommand):
    """Update the properties of the provided virtual machine, or update the tags associated with the virtual machine. Properties and tag updates can be done independently.

    :example: Patch virtual machine
        az networkcloud virtualmachine update --resource-group "resourceGroupName" --name "virtualMachineName" --vm-image-repository-credentials password="password" registry-url="myacr.azurecr.io" username="myuser" --tags key1="myvalue1" key2="myvalue2"
    """

    _aaz_info = {
        "version": "2022-12-12-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.networkcloud/virtualmachines/{}", "2022-12-12-preview"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.virtual_machine_name = AAZStrArg(
            options=["-n", "--name", "--virtual-machine-name"],
            help="The name of the virtual machine.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^([a-zA-Z0-9][a-zA-Z0-9]{0,62}[a-zA-Z0-9])$",
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.vm_image_repository_credentials = AAZObjectArg(
            options=["--vmi-creds", "--vm-image-repository-credentials"],
            arg_group="Properties",
            help="The credentials used to login to the image repository that has access to the specified image.",
        )

        vm_image_repository_credentials = cls._args_schema.vm_image_repository_credentials
        vm_image_repository_credentials.password = AAZStrArg(
            options=["password"],
            help="The password or token used to access an image in the target repository.",
            required=True,
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )
        vm_image_repository_credentials.registry_url = AAZStrArg(
            options=["registry-url"],
            help="The URL of the authentication server used to validate the repository credentials.",
            required=True,
        )
        vm_image_repository_credentials.username = AAZStrArg(
            options=["username"],
            help="The username used to access an image in the target repository.",
            required=True,
            fmt=AAZStrArgFormat(
                min_length=1,
            ),
        )

        # define Arg Group "VirtualMachineUpdateParameters"

        _args_schema = cls._args_schema
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="VirtualMachineUpdateParameters",
            help="The Azure resource tags that will replace the existing ones.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.VirtualMachinesUpdate(ctx=self.ctx)()
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

    class VirtualMachinesUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.NetworkCloud/virtualMachines/{virtualMachineName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PATCH"

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
                **self.serialize_url_param(
                    "virtualMachineName", self.ctx.args.virtual_machine_name,
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
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("vmImageRepositoryCredentials", AAZObjectType, ".vm_image_repository_credentials")

            vm_image_repository_credentials = _builder.get(".properties.vmImageRepositoryCredentials")
            if vm_image_repository_credentials is not None:
                vm_image_repository_credentials.set_prop("password", AAZStrType, ".password", typ_kwargs={"flags": {"required": True, "secret": True}})
                vm_image_repository_credentials.set_prop("registryUrl", AAZStrType, ".registry_url", typ_kwargs={"flags": {"required": True}})
                vm_image_repository_credentials.set_prop("username", AAZStrType, ".username", typ_kwargs={"flags": {"required": True}})

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

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
            _UpdateHelper._build_schema_virtual_machine_read(cls._schema_on_200)

            return cls._schema_on_200


class _UpdateHelper:
    """Helper class for Update"""

    _schema_virtual_machine_read = None

    @classmethod
    def _build_schema_virtual_machine_read(cls, _schema):
        if cls._schema_virtual_machine_read is not None:
            _schema.extended_location = cls._schema_virtual_machine_read.extended_location
            _schema.id = cls._schema_virtual_machine_read.id
            _schema.location = cls._schema_virtual_machine_read.location
            _schema.name = cls._schema_virtual_machine_read.name
            _schema.properties = cls._schema_virtual_machine_read.properties
            _schema.system_data = cls._schema_virtual_machine_read.system_data
            _schema.tags = cls._schema_virtual_machine_read.tags
            _schema.type = cls._schema_virtual_machine_read.type
            return

        cls._schema_virtual_machine_read = _schema_virtual_machine_read = AAZObjectType()

        virtual_machine_read = _schema_virtual_machine_read
        virtual_machine_read.extended_location = AAZObjectType(
            serialized_name="extendedLocation",
            flags={"required": True},
        )
        virtual_machine_read.id = AAZStrType(
            flags={"read_only": True},
        )
        virtual_machine_read.location = AAZStrType(
            flags={"required": True},
        )
        virtual_machine_read.name = AAZStrType(
            flags={"read_only": True},
        )
        virtual_machine_read.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )
        virtual_machine_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        virtual_machine_read.tags = AAZDictType()
        virtual_machine_read.type = AAZStrType(
            flags={"read_only": True},
        )

        extended_location = _schema_virtual_machine_read.extended_location
        extended_location.name = AAZStrType(
            flags={"required": True},
        )
        extended_location.type = AAZStrType(
            flags={"required": True},
        )

        properties = _schema_virtual_machine_read.properties
        properties.admin_username = AAZStrType(
            serialized_name="adminUsername",
            flags={"required": True},
        )
        properties.bare_metal_machine_id = AAZStrType(
            serialized_name="bareMetalMachineId",
            flags={"read_only": True},
        )
        properties.boot_method = AAZStrType(
            serialized_name="bootMethod",
        )
        properties.cloud_services_network_attachment = AAZObjectType(
            serialized_name="cloudServicesNetworkAttachment",
            flags={"required": True},
        )
        properties.cluster_id = AAZStrType(
            serialized_name="clusterId",
            flags={"read_only": True},
        )
        properties.cpu_cores = AAZIntType(
            serialized_name="cpuCores",
            flags={"required": True},
        )
        properties.detailed_status = AAZStrType(
            serialized_name="detailedStatus",
            flags={"read_only": True},
        )
        properties.detailed_status_message = AAZStrType(
            serialized_name="detailedStatusMessage",
            flags={"read_only": True},
        )
        properties.isolate_emulator_thread = AAZStrType(
            serialized_name="isolateEmulatorThread",
        )
        properties.memory_size_gb = AAZIntType(
            serialized_name="memorySizeGB",
            flags={"required": True},
        )
        properties.network_attachments = AAZListType(
            serialized_name="networkAttachments",
        )
        properties.network_data = AAZStrType(
            serialized_name="networkData",
        )
        properties.placement_hints = AAZListType(
            serialized_name="placementHints",
        )
        properties.power_state = AAZStrType(
            serialized_name="powerState",
            flags={"read_only": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.ssh_public_keys = AAZListType(
            serialized_name="sshPublicKeys",
        )
        properties.storage_profile = AAZObjectType(
            serialized_name="storageProfile",
            flags={"required": True},
        )
        properties.user_data = AAZStrType(
            serialized_name="userData",
        )
        properties.virtio_interface = AAZStrType(
            serialized_name="virtioInterface",
        )
        properties.vm_device_model = AAZStrType(
            serialized_name="vmDeviceModel",
        )
        properties.vm_image = AAZStrType(
            serialized_name="vmImage",
            flags={"required": True},
        )
        properties.vm_image_repository_credentials = AAZObjectType(
            serialized_name="vmImageRepositoryCredentials",
        )
        properties.volumes = AAZListType(
            flags={"read_only": True},
        )

        cloud_services_network_attachment = _schema_virtual_machine_read.properties.cloud_services_network_attachment
        cloud_services_network_attachment.attached_network_id = AAZStrType(
            serialized_name="attachedNetworkId",
            flags={"required": True},
        )
        cloud_services_network_attachment.default_gateway = AAZStrType(
            serialized_name="defaultGateway",
        )
        cloud_services_network_attachment.ip_allocation_method = AAZStrType(
            serialized_name="ipAllocationMethod",
            flags={"required": True},
        )
        cloud_services_network_attachment.ipv4_address = AAZStrType(
            serialized_name="ipv4Address",
        )
        cloud_services_network_attachment.ipv6_address = AAZStrType(
            serialized_name="ipv6Address",
        )
        cloud_services_network_attachment.mac_address = AAZStrType(
            serialized_name="macAddress",
            flags={"read_only": True},
        )
        cloud_services_network_attachment.network_attachment_name = AAZStrType(
            serialized_name="networkAttachmentName",
        )

        network_attachments = _schema_virtual_machine_read.properties.network_attachments
        network_attachments.Element = AAZObjectType()

        _element = _schema_virtual_machine_read.properties.network_attachments.Element
        _element.attached_network_id = AAZStrType(
            serialized_name="attachedNetworkId",
            flags={"required": True},
        )
        _element.default_gateway = AAZStrType(
            serialized_name="defaultGateway",
        )
        _element.ip_allocation_method = AAZStrType(
            serialized_name="ipAllocationMethod",
            flags={"required": True},
        )
        _element.ipv4_address = AAZStrType(
            serialized_name="ipv4Address",
        )
        _element.ipv6_address = AAZStrType(
            serialized_name="ipv6Address",
        )
        _element.mac_address = AAZStrType(
            serialized_name="macAddress",
            flags={"read_only": True},
        )
        _element.network_attachment_name = AAZStrType(
            serialized_name="networkAttachmentName",
        )

        placement_hints = _schema_virtual_machine_read.properties.placement_hints
        placement_hints.Element = AAZObjectType()

        _element = _schema_virtual_machine_read.properties.placement_hints.Element
        _element.hint_type = AAZStrType(
            serialized_name="hintType",
            flags={"required": True},
        )
        _element.resource_id = AAZStrType(
            serialized_name="resourceId",
            flags={"required": True},
        )
        _element.scheduling_execution = AAZStrType(
            serialized_name="schedulingExecution",
            flags={"required": True},
        )
        _element.scope = AAZStrType(
            flags={"required": True},
        )

        ssh_public_keys = _schema_virtual_machine_read.properties.ssh_public_keys
        ssh_public_keys.Element = AAZObjectType()

        _element = _schema_virtual_machine_read.properties.ssh_public_keys.Element
        _element.key_data = AAZStrType(
            serialized_name="keyData",
            flags={"required": True},
        )

        storage_profile = _schema_virtual_machine_read.properties.storage_profile
        storage_profile.os_disk = AAZObjectType(
            serialized_name="osDisk",
            flags={"required": True},
        )
        storage_profile.volume_attachments = AAZListType(
            serialized_name="volumeAttachments",
        )

        os_disk = _schema_virtual_machine_read.properties.storage_profile.os_disk
        os_disk.create_option = AAZStrType(
            serialized_name="createOption",
        )
        os_disk.delete_option = AAZStrType(
            serialized_name="deleteOption",
        )
        os_disk.disk_size_gb = AAZIntType(
            serialized_name="diskSizeGB",
            flags={"required": True},
        )

        volume_attachments = _schema_virtual_machine_read.properties.storage_profile.volume_attachments
        volume_attachments.Element = AAZStrType()

        vm_image_repository_credentials = _schema_virtual_machine_read.properties.vm_image_repository_credentials
        vm_image_repository_credentials.password = AAZStrType(
            flags={"required": True, "secret": True},
        )
        vm_image_repository_credentials.registry_url = AAZStrType(
            serialized_name="registryUrl",
            flags={"required": True},
        )
        vm_image_repository_credentials.username = AAZStrType(
            flags={"required": True},
        )

        volumes = _schema_virtual_machine_read.properties.volumes
        volumes.Element = AAZStrType()

        system_data = _schema_virtual_machine_read.system_data
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

        tags = _schema_virtual_machine_read.tags
        tags.Element = AAZStrType()

        _schema.extended_location = cls._schema_virtual_machine_read.extended_location
        _schema.id = cls._schema_virtual_machine_read.id
        _schema.location = cls._schema_virtual_machine_read.location
        _schema.name = cls._schema_virtual_machine_read.name
        _schema.properties = cls._schema_virtual_machine_read.properties
        _schema.system_data = cls._schema_virtual_machine_read.system_data
        _schema.tags = cls._schema_virtual_machine_read.tags
        _schema.type = cls._schema_virtual_machine_read.type


__all__ = ["Update"]
