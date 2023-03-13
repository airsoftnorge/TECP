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
from gpiozero import Buzzer

import meshtastic
import meshtastic.serial_interface

# set up GPIO pins for buttons
# 17 being red
# 22 being blue
# 27 being yellow (or neutral)
# 23 being buzzer

bz = Buzzer(23)
red_button = Button(17, bounce_time=0.2)
blue_button = Button(22, bounce_time=0.2)
yellow_button = Button(27, bounce_time=0.2)

# Setup all default values:
name = ""
mode = ""
capture_time = 30
startcolor = ""
hasbuzzer = 0
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

def buzzercapcomplete():
    print(f"Playing capture sound")
    for i in range(5):
        bz.on()
        print(f"BEEP")
        time.sleep(0.25)
        bz.off()
        time.sleep(0.25)

# send initial state
def send_initial_state():
    print(f"Sending initial state of the point")
    # create a message to send in meshtastic
    sendmessage(f"/mesh/points/{name}/{mode}/status/{startcolor}")
    print(f"Initial message sent")

#Sending initial state from config.json
print(f"Point: {name}")
print(f"Mode: {mode}")
print(f"Starts as: {mode}")
print(f"Capture time: {capture_time}")
print(f"Buzzer: {hasbuzzer}")
send_initial_state()

def button_pressed(color):
    global start_time
    # check if this is the first time the button is pressed
    if start_time == 0:
        start_time = time.time()
    # check if the button has been held for 30 seconds
    if time.time() - start_time >= capture_time:
        print(f"Point {name} has been captured by {color}!")
        sendmessage(f"/mesh/points/{name}/{mode}/status/{color}")
        # play capture buzz if enabled
        if hasbuzzer == 1:
            buzzercapcomplete()
        time.sleep(5)
        # reset the start time
        start_time = 0
    else:
        timeheld = time.time() - start_time
        print(f"Capture started for {color}. Held for {int(timeheld)}seconds.")
        time.sleep(2)
    return start_time

# loop forever
print(f"Starting looping forever")

while True:
    # check if red_button is held
    if red_button.is_pressed:
        start_time = button_pressed("red")
    # check if blue_button is held
    elif blue_button.is_pressed:
        start_time = button_pressed("blue")
    # check if yellow_button is held
    elif yellow_button.is_pressed:
        start_time = button_pressed("yellow")
    # no button is pressed, reset start time
    else:
        start_time = 0
    # sleep for a short amount of time to avoid consuming too much CPU
    time.sleep(0.1)
