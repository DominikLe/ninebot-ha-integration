# Ninebot Scooter integration for Home Assistant

> **This is a fork** of [ownbee/ninebot-integration](https://github.com/ownbee/ninebot-integration), maintained here with bug fixes,
> CI validation, and packaging improvements. See the [Changelog](#changelog) below for what changed
> compared to upstream.
>
> **AI disclosure:** Changes in this fork (fixes, tests, CI, packaging, this README) were made with
> AI assistance (Claude). Fixes were verified against a real Home Assistant instance and a physical
> scooter where noted in the changelog; review the code yourself before relying on it.

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

### 0.0.3

- Fixed the Bluetooth-discovery confirmation dialog rendering with an empty body
  (no `strings.json`/`translations` shipped with the integration at all).
- Added a CI pipeline (hassfest, HACS validation, unit tests) that runs on every
  push/PR and daily.
- Added unit tests for the pure conversion logic (`device.py`, `sensor.py`) so
  regressions like the 0.0.2 setup bug get caught automatically.
- Added a `documentation`/`issue_tracker` link and sorted keys in `manifest.json`
  (required by hassfest).
- Added `LICENSE` (MIT) and repository topics (required for HACS validation).
- Added an original brand icon (`custom_components/ninebot_scooter/brand/`).
- Repository is now public so HACS custom-repository installs work without a
  personal access token.

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
