import RPi.GPIO as GPIO
import time
from meshtastic import SerialInterface, MessageType
import json

# set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# set up GPIO pins for buttons
# 17 being red
# 22 being blue
# 27 being yellow (or neutral)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# set up dummy variables to be loaded from json
name = ""
mode = ""
capture_time = ""
startcolor = ""


# load the configuration data from the JSON file
with open("config.json", "r") as f:
    config_data = json.load(f)

#Get keys from config
for key, value in config_data.items():
    globals()[key] = value

# set up initial button states

button_states = {
    17: False,
    22: False,
    27: False
}

# connect to meshtastic
interface = SerialInterface()

# send initial state
def sendinitialstate():
    print(f"Sending initial state of the point")
    # create a message to send in meshtastic
    message = MessageType.TEXT_ONLY.value()
    message["data"]["text"] = f"{startcolor}"
    message["rxfs"] = [f"/mesh/points/{mode}/{name}/status/"]
    # send the message in meshtastic
    interface.sendData(message)
sendinitialstate()

# loop forever
while True:
    # check if each button is pressed
    for pin, buttoncolor in [(17, "red"), (22, "blue"), (27, "yellow")]:
        if not GPIO.input(pin):
            # button is pressed, start counting
            button_states[pin] = time.time()
        elif button_states[pin] and time.time() - button_states[pin] >= 30:
            # button was pressed for more than 30 seconds
            print(f"Button {buttoncolor} was pressed for over 30 seconds")

            # create a message to send in meshtastic
            message = MessageType.TEXT_ONLY.value()
            message["data"]["text"] = f"{buttoncolor}"
            message["rxfs"] = [f"/mesh/points/{mode}/{name}/status/"]

            # send the message in meshtastic
            interface.sendData(message)

            button_states[pin] = False

    # wait a short time before checking again
    time.sleep(0.1)