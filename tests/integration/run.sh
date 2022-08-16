#!/usr/bin/env bash

if [[ "$CI" == "true" ]]
then
  export $(dbus-launch)
  echo "" | gnome-keyring-daemon --unlock
fi

python3 -m pytest tests/integration/
