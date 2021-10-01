import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID

AUTO_LOAD = ["sensor", "text_sensor", "binary_sensor"]

DEPENDENCIES = ["uart"]

CODEOWNERS = ["@KinDR007"]

MULTI_CONF = True

victron_ns = cg.esphome_ns.namespace("victron")
VictronComponent = victron_ns.class_("VictronComponent", uart.UARTDevice, cg.Component)

CONF_VICTRON_ID = "victron_id"

CONFIG_SCHEMA = uart.UART_DEVICE_SCHEMA.extend(
    {
        cv.GenerateID(): cv.declare_id(VictronComponent),
    }
)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield uart.register_uart_device(var, config)
