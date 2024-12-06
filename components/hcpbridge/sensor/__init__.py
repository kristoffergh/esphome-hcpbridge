from esphome.components import sensor
import esphome.config_validation as cv
import esphome.codegen as cg
from esphome.const import UNIT_PERCENT, ICON_PERCENT, STATE_CLASS_MEASUREMENT, CONF_ID
from .. import hcpbridge_ns, HCPBridge, CONF_HCPBridge_ID

DEPENDENCIES = ["hcpbridge"]

HCPBridgeSensor = hcpbridge_ns.class_("HCPBridgeSensor", sensor.Sensor, cg.Component)

CONFIG_SCHEMA = (
    sensor.sensor_schema(
        unit_of_measurement=UNIT_PERCENT,
        icon=ICON_PERCENT,
        state_class=STATE_CLASS_MEASUREMENT,
        accuracy_decimals=0,
    )
    .extend({cv.GenerateID(): cv.declare_id(HCPBridgeSensor)})
    .extend({cv.GenerateID(CONF_HCPBridge_ID): cv.use_id(HCPBridge)})
    .extend(cv.COMPONENT_SCHEMA)
)

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    parent = await cg.get_variable(config[CONF_HCPBridge_ID])
    cg.add(var.set_hcpbridge_parent(parent))
    await cg.register_component(var, config)
    await sensor.register_sensor(var, config)
