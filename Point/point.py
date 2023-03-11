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

red_button = Button(17, pull_up=False, bounce_time=0.1)
blue_button = Button(22, pull_up=False, bounce_time=0.1)
yellow_button = Button(27, pull_up=False, bounce_time=0.1)

# set up dummy variables to be loaded from json
name = ""
mode = ""
capture_time = ""
startcolor = ""

# load the configuration data from the JSON file
with open("config.json", "r") as f:
    config_data = json.load(f)

# Get keys from config
for key, value in config_data.items():
    globals()[key] = value

# set up initial button states
button_states = {
    17: False,
    22: False,
    27: False
}

# connect to meshtastic
def sendmessage(poop):
    iface = meshtastic.serial_interface.SerialInterface()
    iface.sendText(poop)
    iface.close()

# send initial state
def send_initial_state():
    print(f"Sending initial state of the point")
    # create a message to send in meshtastic
    sendmessage(f"/mesh/points/{mode}/{name}/status/{startcolor}")
    print(f"Initial message sent")
send_initial_state()

# loop forever
print(f"Starting looping forever")

while True:
    # check if each button is pressed
    for button, buttoncolor in [(red_button, "red"), (blue_button, "blue"), (yellow_button, "yellow")]:
        if button.is_pressed:
            # button is pressed, start counting
            button_states[button.pin.number] = time.time()
        elif button_states[button.pin.number] and time.time() - button_states[button.pin.number] >= capture_time:
            # button was pressed for more than capturetime specified seconds
            print(f"Button {buttoncolor} was pressed for over {capture_time} seconds")
            # create a message to send in meshtastic
            sendmessage(f"/mesh/points/{mode}/{name}/status/{buttoncolor}")
            button_states[button.pin.number] = False
    # wait a short time before checking again
    time.sleep(0.1)
