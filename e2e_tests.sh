#!/usr/bin/env bash
set -euo pipefail

APPIUM_PID=""

terminate_crashpad_handler() {  
  if [ -n "$APPIUM_PID" ]; then
      echo "Stopping Appium process: $APPIUM_PID"
      kill "$APPIUM_PID" || true
  fi
  
  echo "Executing aggressive crashpad_handler cleanup..."
  pkill -f -SIGTERM crashpad_handler || true

  sleep 5
  if pgrep -f crashpad_handler >/dev/null; then
    echo "crashpad_handler still active, forcing kill ☠️..."
    pkill -f -SIGKILL crashpad_handler || true
  fi
}

trap terminate_crashpad_handler EXIT

appium --allow-insecure="*:chromedriver_autodownload" --allow-cors --log-level info &
APPIUM_PID=$!
echo "Appium started with PID: $APPIUM_PID"

pytest -s
TEST_EXIT_CODE=$?

exit $TEST_EXIT_CODE