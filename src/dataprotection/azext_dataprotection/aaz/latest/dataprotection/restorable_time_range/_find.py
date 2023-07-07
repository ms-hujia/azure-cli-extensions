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
    "dataprotection restorable-time-range find",
    is_experimental=True,
)
class Find(AAZCommand):
    """Finds the valid recovery point in time ranges for the restore.

    :example: Find Restorable Time Ranges
        az dataprotection restorable-time-range find --backup-instance-name "zblobbackuptestsa58" --end-time "2021-02-24T00:35:17.6829685Z" --source-data-store-type "OperationalStore" --start-time "2020-10-17T23:28:17.6829685Z" --resource-group "Blob-Backup" --vault-name "ZBlobBackupVaultBVTD3"
    """

    _aaz_info = {
        "version": "2023-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.dataprotection/backupvaults/{}/backupinstances/{}/findrestorabletimeranges", "2023-01-01"],
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
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.end_time = AAZStrArg(
            options=["--end-time"],
            help="End time for the List Restore Ranges request. ISO 8601 format.",
        )
        _args_schema.source_data_store_type = AAZStrArg(
            options=["--source-data-store-type"],
            help="Gets or sets the type of the source data store.",
            required=True,
            enum={"ArchiveStore": "ArchiveStore", "OperationalStore": "OperationalStore", "VaultStore": "VaultStore"},
        )
        _args_schema.start_time = AAZStrArg(
            options=["--start-time"],
            help="Start time for the List Restore Ranges request. ISO 8601 format.",
        )

        # define Arg Group "Resource Id"

        _args_schema = cls._args_schema
        _args_schema.backup_instance_name = AAZStrArg(
            options=["--backup-instance-name"],
            arg_group="Resource Id",
            help="The name of the backup instance.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.vault_name = AAZStrArg(
            options=["--vault-name"],
            arg_group="Resource Id",
            help="The name of the backup vault.",
            required=True,
            id_part="name",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.RestorableTimeRangesFind(ctx=self.ctx)()
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

    class RestorableTimeRangesFind(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DataProtection/backupVaults/{vaultName}/backupInstances/{backupInstanceName}/findRestorableTimeRanges",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "backupInstanceName", self.ctx.args.backup_instance_name,
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
                **self.serialize_url_param(
                    "vaultName", self.ctx.args.vault_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-01-01",
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
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("endTime", AAZStrType, ".end_time")
            _builder.set_prop("sourceDataStoreType", AAZStrType, ".source_data_store_type", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("startTime", AAZStrType, ".start_time")

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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType()
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.object_type = AAZStrType(
                serialized_name="objectType",
            )
            properties.restorable_time_ranges = AAZListType(
                serialized_name="restorableTimeRanges",
            )

            restorable_time_ranges = cls._schema_on_200.properties.restorable_time_ranges
            restorable_time_ranges.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.restorable_time_ranges.Element
            _element.end_time = AAZStrType(
                serialized_name="endTime",
                flags={"required": True},
            )
            _element.object_type = AAZStrType(
                serialized_name="objectType",
            )
            _element.start_time = AAZStrType(
                serialized_name="startTime",
                flags={"required": True},
            )

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

            return cls._schema_on_200


class _FindHelper:
    """Helper class for Find"""


__all__ = ["Find"]
