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
    "networkcloud racksku show",
    is_preview=True,
)
class Show(AAZCommand):
    """Get the properties of the provided rack SKU.

    :example: Get rack SKU resource
        az networkcloud racksku show --name "rackSkuName"
    """

    _aaz_info = {
        "version": "2024-06-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/providers/microsoft.networkcloud/rackskus/{}", "2024-06-01-preview"],
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
        _args_schema.rack_sku_name = AAZStrArg(
            options=["-n", "--name", "--rack-sku-name"],
            help="The name of the rack SKU.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^([a-zA-Z0-9][a-zA-Z0-9-_]{0,126}[a-zA-Z0-9])$",
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.RackSkusGet(ctx=self.ctx)()
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

    class RackSkusGet(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/providers/Microsoft.NetworkCloud/rackSkus/{rackSkuName}",
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
                    "rackSkuName", self.ctx.args.rack_sku_name,
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
                    "api-version", "2024-06-01-preview",
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
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
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
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.compute_machines = AAZListType(
                serialized_name="computeMachines",
                flags={"read_only": True},
            )
            properties.controller_machines = AAZListType(
                serialized_name="controllerMachines",
                flags={"read_only": True},
            )
            properties.description = AAZStrType(
                flags={"read_only": True},
            )
            properties.max_cluster_slots = AAZIntType(
                serialized_name="maxClusterSlots",
                flags={"read_only": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.rack_type = AAZStrType(
                serialized_name="rackType",
                flags={"read_only": True},
            )
            properties.storage_appliances = AAZListType(
                serialized_name="storageAppliances",
                flags={"read_only": True},
            )
            properties.supported_rack_sku_ids = AAZListType(
                serialized_name="supportedRackSkuIds",
                flags={"read_only": True},
            )

            compute_machines = cls._schema_on_200.properties.compute_machines
            compute_machines.Element = AAZObjectType()
            _ShowHelper._build_schema_machine_sku_slot_read(compute_machines.Element)

            controller_machines = cls._schema_on_200.properties.controller_machines
            controller_machines.Element = AAZObjectType()
            _ShowHelper._build_schema_machine_sku_slot_read(controller_machines.Element)

            storage_appliances = cls._schema_on_200.properties.storage_appliances
            storage_appliances.Element = AAZObjectType()

            _element = cls._schema_on_200.properties.storage_appliances.Element
            _element.properties = AAZObjectType(
                flags={"client_flatten": True},
            )
            _element.rack_slot = AAZIntType(
                serialized_name="rackSlot",
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties.storage_appliances.Element.properties
            properties.capacity_gb = AAZIntType(
                serialized_name="capacityGB",
                flags={"read_only": True},
            )
            properties.model = AAZStrType(
                flags={"read_only": True},
            )

            supported_rack_sku_ids = cls._schema_on_200.properties.supported_rack_sku_ids
            supported_rack_sku_ids.Element = AAZStrType()

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


class _ShowHelper:
    """Helper class for Show"""

    _schema_machine_sku_slot_read = None

    @classmethod
    def _build_schema_machine_sku_slot_read(cls, _schema):
        if cls._schema_machine_sku_slot_read is not None:
            _schema.properties = cls._schema_machine_sku_slot_read.properties
            _schema.rack_slot = cls._schema_machine_sku_slot_read.rack_slot
            return

        cls._schema_machine_sku_slot_read = _schema_machine_sku_slot_read = AAZObjectType()

        machine_sku_slot_read = _schema_machine_sku_slot_read
        machine_sku_slot_read.properties = AAZObjectType(
            flags={"client_flatten": True},
        )
        machine_sku_slot_read.rack_slot = AAZIntType(
            serialized_name="rackSlot",
            flags={"read_only": True},
        )

        properties = _schema_machine_sku_slot_read.properties
        properties.bootstrap_protocol = AAZStrType(
            serialized_name="bootstrapProtocol",
            flags={"read_only": True},
        )
        properties.cpu_cores = AAZIntType(
            serialized_name="cpuCores",
            flags={"read_only": True},
        )
        properties.cpu_sockets = AAZIntType(
            serialized_name="cpuSockets",
            flags={"read_only": True},
        )
        properties.disks = AAZListType(
            flags={"read_only": True},
        )
        properties.generation = AAZStrType(
            flags={"read_only": True},
        )
        properties.hardware_version = AAZStrType(
            serialized_name="hardwareVersion",
            flags={"read_only": True},
        )
        properties.memory_capacity_gb = AAZIntType(
            serialized_name="memoryCapacityGB",
            flags={"read_only": True},
        )
        properties.model = AAZStrType(
            flags={"read_only": True},
        )
        properties.network_interfaces = AAZListType(
            serialized_name="networkInterfaces",
            flags={"read_only": True},
        )
        properties.total_threads = AAZIntType(
            serialized_name="totalThreads",
            flags={"read_only": True},
        )
        properties.vendor = AAZStrType(
            flags={"read_only": True},
        )

        disks = _schema_machine_sku_slot_read.properties.disks
        disks.Element = AAZObjectType()

        _element = _schema_machine_sku_slot_read.properties.disks.Element
        _element.capacity_gb = AAZIntType(
            serialized_name="capacityGB",
            flags={"read_only": True},
        )
        _element.connection = AAZStrType(
            flags={"read_only": True},
        )
        _element.type = AAZStrType(
            flags={"read_only": True},
        )

        network_interfaces = _schema_machine_sku_slot_read.properties.network_interfaces
        network_interfaces.Element = AAZObjectType()

        _element = _schema_machine_sku_slot_read.properties.network_interfaces.Element
        _element.address = AAZStrType(
            flags={"read_only": True},
        )
        _element.device_connection_type = AAZStrType(
            serialized_name="deviceConnectionType",
            flags={"read_only": True},
        )
        _element.model = AAZStrType(
            flags={"read_only": True},
        )
        _element.physical_slot = AAZIntType(
            serialized_name="physicalSlot",
            flags={"read_only": True},
        )
        _element.port_count = AAZIntType(
            serialized_name="portCount",
            flags={"read_only": True},
        )
        _element.port_speed = AAZIntType(
            serialized_name="portSpeed",
            flags={"read_only": True},
        )
        _element.vendor = AAZStrType(
            flags={"read_only": True},
        )

        _schema.properties = cls._schema_machine_sku_slot_read.properties
        _schema.rack_slot = cls._schema_machine_sku_slot_read.rack_slot


__all__ = ["Show"]
