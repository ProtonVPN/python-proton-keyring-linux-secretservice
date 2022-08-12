#!/usr/bin/env bash

export $(dbus-launch)
echo "" | gnome-keyring-daemon --unlock
python3 -m pytest tests/integration/