import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import (
    CONF_ID,
)
from . import VictronComponent, CONF_VICTRON_ID

DEPENDENCIES = ["victron"]

CODEOWNERS = ["@KinDR007"]

CONF_LOAD_OUTPUT_STATE = "load_output_state"

BINARY_SENSORS = [
    CONF_LOAD_OUTPUT_STATE,
]

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_VICTRON_ID): cv.use_id(VictronComponent),
        cv.Optional(CONF_LOAD_OUTPUT_STATE): binary_sensor.BINARY_SENSOR_SCHEMA.extend(
            {cv.GenerateID(): cv.declare_id(binary_sensor.BinarySensor)}
        ),
    }
)


def to_code(config):
    hub = yield cg.get_variable(config[CONF_VICTRON_ID])
    for key in BINARY_SENSORS:
        if key in config:
            conf = config[key]
            sens = cg.new_Pvariable(conf[CONF_ID])
            yield binary_sensor.register_binary_sensor(sens, conf)
            cg.add(getattr(hub, f"set_{key}_binary_sensor")(sens))