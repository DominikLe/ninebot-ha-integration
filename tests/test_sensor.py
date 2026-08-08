from ninebot_ble import (
    DeviceKey,
    SensorDescription,
    SensorDeviceClass,
    SensorDeviceInfo,
    SensorUpdate,
    SensorValue,
    Units,
)

from custom_components.ninebot_scooter.sensor import sensor_update_to_bluetooth_data_update

ADDRESS = "AA:BB:CC:DD:EE:FF"


def _sensor_update() -> SensorUpdate:
    battery_key = DeviceKey(key="battery_voltage", device_id=ADDRESS)
    return SensorUpdate(
        title="NinebotMax",
        devices={
            ADDRESS: SensorDeviceInfo(
                name="NinebotMax",
                model="Max",
                manufacturer="Ninebot",
                sw_version="1.1.8",
                hw_version=None,
            )
        },
        entity_descriptions={
            battery_key: SensorDescription(
                device_key=battery_key,
                device_class=SensorDeviceClass.VOLTAGE,
                native_unit_of_measurement=Units.ELECTRIC_POTENTIAL_VOLT,
            )
        },
        entity_values={
            battery_key: SensorValue(device_key=battery_key, name="Battery voltage", native_value=36.52),
        },
    )


def test_converts_devices():
    update = sensor_update_to_bluetooth_data_update(_sensor_update())

    assert ADDRESS in update.devices
    assert update.devices[ADDRESS]["name"] == "NinebotMax"
    assert update.devices[ADDRESS]["model"] == "Max"


def test_converts_entity_values_and_names():
    update = sensor_update_to_bluetooth_data_update(_sensor_update())

    (entity_key,) = update.entity_data.keys()
    assert entity_key.key == "battery_voltage"
    assert entity_key.device_id == ADDRESS
    assert update.entity_data[entity_key] == 36.52
    assert update.entity_names[entity_key] == "Battery voltage"


def test_converts_entity_descriptions():
    update = sensor_update_to_bluetooth_data_update(_sensor_update())

    (description,) = update.entity_descriptions.values()
    assert description.device_class == "voltage"
    assert description.native_unit_of_measurement == "V"


def test_entity_description_device_class_none_when_not_set():
    battery_key = DeviceKey(key="alarm_code", device_id=ADDRESS)
    sensor_update = SensorUpdate(
        title="NinebotMax",
        devices={},
        entity_descriptions={
            battery_key: SensorDescription(device_key=battery_key, device_class=None, native_unit_of_measurement=None)
        },
        entity_values={battery_key: SensorValue(device_key=battery_key, name="Alarm code", native_value=0)},
    )

    update = sensor_update_to_bluetooth_data_update(sensor_update)

    (description,) = update.entity_descriptions.values()
    assert description.device_class is None
