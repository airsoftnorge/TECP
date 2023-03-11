#
#     ______   ______   ______   ____
#    /_  __/  / ____/  / ____/  / __ \
#     / /    / __/    / /      / /_/ /
#    / /    / /___   / /___   / ____/
#   /_/    /_____/   \____/  /_/
#
#
# There is no differentiation based on mode currently, as this is expected to be for expansion or mostly handled by the gateway.


import sys
import json
import time

from gpiozero import Button
import meshtastic
import meshtastic.serial_interface

# set up GPIO pins for buttons
# 17 being red
# 22 being blue
# 27 being yellow (or neutral)

red_button = Button(17, bounce_time=0.2)
blue_button = Button(22, bounce_time=0.2)
yellow_button = Button(27, bounce_time=0.2)

# Setup all default values:
name = ""
mode = ""
capture_time = ""
startcolor = ""
start_time = 0

# load the configuration data from the JSON file
with open("config.json", "r") as f:
    config_data = json.load(f)

# Get keys from config
for key, value in config_data.items():
    globals()[key] = value

# connect to meshtastic
def sendmessage(poop):
    iface = meshtastic.serial_interface.SerialInterface()
    iface.sendText(poop)
    iface.close()

# send initial state
def send_initial_state():
    print(f"Sending initial state of the point")
    # create a message to send in meshtastic
    sendmessage(f"/mesh/points/{name}/{mode}/status/{startcolor}")
    print(f"Initial message sent")
send_initial_state()

# loop forever
print(f"Starting looping forever")

while True:
    # check if red_button is held
    if red_button.is_pressed:
        # check if this is the first time the button is pressed
        if start_time == 0:
            start_time = time.time()
        # check if the button has been held for 30 seconds
        if time.time() - start_time >= 30:
            sendmessage(f"/mesh/points/{name}/{mode}/status/red")
            # reset the start time
            start_time = 0
    # check if blue_button is held
    elif blue_button.is_pressed:
        # check if this is the first time the button is pressed
        if start_time == 0:
            start_time = time.time()
        # check if the button has been held for 30 seconds
        if time.time() - start_time >= 30:
            print("Sending blue to meshtastic!")
            sendmessage(f"/mesh/points/{name}/{mode}/status/blue")
            # reset the start time
            start_time = 0
    elif yellow_button.is_pressed:
        print("Yellow button detected")
        # check if this is the first time the button is pressed
        if start_time == 0:
            start_time = time.time()
        # check if the button has been held for 30 seconds
        if time.time() - start_time >= 30:
            print("Sending yellow to meshtastic!")
            sendmessage(f"/mesh/points/{name}/{mode}/status/yellow")
            # reset the start time
            start_time = 0
    # no button is pressed, reset start time
    else:
        start_time = 0

    # sleep for a short amount of time to avoid consuming too much CPU
    time.sleep(0.1)


