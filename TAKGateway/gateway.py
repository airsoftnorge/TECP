#
#     ______   ______   ______   ____
#    /_  __/  / ____/  / ____/  / __ \
#     / /    / __/    / /      / /_/ /
#    / /    / /___   / /___   / ____/
#   /_/    /_____/   \____/  /_/
#
# Gateway is responsible for feeding node-red with meshtastic events. Does not work standalone.

import sys
import json
import time
import meshtastic
import meshtastic.serial_interface
