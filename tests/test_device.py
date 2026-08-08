from ninebot_ble import DeviceKey

from custom_components.ninebot_scooter.device import device_key_to_bluetooth_entity_key


def test_maps_key_and_device_id():
    device_key = DeviceKey(key="battery_voltage", device_id="AA:BB:CC:DD:EE:FF")

    entity_key = device_key_to_bluetooth_entity_key(device_key)

    assert entity_key.key == "battery_voltage"
    assert entity_key.device_id == "AA:BB:CC:DD:EE:FF"


def test_device_id_defaults_to_none():
    entity_key = device_key_to_bluetooth_entity_key(DeviceKey(key="alarm_code"))

    assert entity_key.device_id is None
