# Ninebot Scooter integration for Home Assistant

**NOTE: This integration is in an alpha state. Feel free to fork or help pushing PRs improving this integration.**

It connects and polls data from a Ninebot Scooter using BLE.

## Manual installation

1. Copy the directory `custom_components/ninebot_scooter` into you installation under
   `<config_dir>/custom_components`.

2. Restart home assistant.

## Changelog

### 0.0.2

- Fixed `NinebotBluetoothSensorEntity` failing to set up on current Home Assistant
  core versions: `PassiveBluetoothDataProcessor` now takes two type parameters
  (`_T`, `_DataT`), and this integration only supplied one. This was likely the
  root cause behind "Error setting up entry" reports. Fixed with the correct
  second type argument (`SensorUpdate`) instead of the placeholder `1` used in a
  community fork's workaround.
- Removed an unused, dead import in `__init__.py`.
- Bumped `ninebot-ble` to `0.0.6` (latest release).
- Added `hacs.json` so the repository validates correctly for HACS custom
  repository installs.
