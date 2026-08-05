# Ninebot Scooter integration for Home Assistant

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=DominikLe&repository=ninebot-ha-integration&category=integration)

**NOTE: This integration is in an alpha state. Feel free to fork or help pushing PRs improving this integration.**

It connects and polls data from a Ninebot Scooter using BLE.

## Installation

### HACS

Click the badge above, or add this repository as a custom repository in HACS
manually (category: Integration), then install "Ninebot Scooter" from HACS.

### Manual

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
