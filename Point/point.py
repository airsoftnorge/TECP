#
#     ______   ______   ______   ____
#    /_  __/  / ____/  / ____/  / __ \
#     / /    / __/    / /      / /_/ /
#    / /    / /___   / /___   / ____/
#   /_/    /_____/   \____/  /_/
#
#


import json
import math
import time

import meshtastic
import meshtastic.serial_interface
from gpiozero import Button
from gpiozero import Buzzer
from rpi_lcd import LCD

lcd = LCD()

# load the configuration data from the JSON file
with open("config.json", "r") as f:
    config_data = json.load(f)
    print("Loaded config:")
    for key, value in config_data.items():
        globals()[key] = value
        print(f"{key}:{value}")

# Set up variables:
spawn_last_spam = time.time()
spawn_cycle_timer_start = time.time()
capture_self_reset_when = float(time.time() + 99999)
capture_time = float(capture_time)
point_refresh_cycle = float(point_refresh_cycle)
color = str(start_color)
point_refresh_time = time.time()
# set up GPIO pins for buttons
bz = Buzzer(23)
red_button = Button(17, bounce_time=0.025)
blue_button = Button(22, bounce_time=0.025)
yellow_button = Button(27, bounce_time=0.025)

# Clear any LCD junk if you have it...
lcd.clear()


def capture_self_reset_triggered():
    send_initial_state()
    capture_set_self_reset_when()
    buzzer_cap_complete()


def capture_set_self_reset_when():
    if capture_self_reset == 1:
        self_reset_when = time.time()
        return self_reset_when


def send_message(text):
    iface = meshtastic.serial_interface.SerialInterface()
    iface.sendText(text)
    iface.close()


def buzzer_cap_complete():
    print(f"Playing capture sound")
    if has_buzzer == 1:
        print("BE BE BE BEEP")
        for i in range(3):
            bz.on()
            time.sleep(0.1)
            bz.off()
            time.sleep(0.1)
        bz.on()
        time.sleep(0.2)
        bz.off()


def buzzer_spawn_cycle():
    global spawn_cycle_timer_start
    print(f"Time for a {mode} respawn!")
    for i in range(5):
        bz.on()
        print(f"BEEP")
        time.sleep(0.25)
        bz.off()
        time.sleep(0.1)
    print(f"Resetting spawn cycle!")
    spawn_cycle_timer_start = time.time()
    return spawn_cycle_timer_start


def displaytext(text, line):
    if display == 1:
        lcd.text(text, line)


def set_color(newcolor):
    global color
    color = newcolor


def capture_complete(teamcolor):
    print(f"Point {name} has been captured by {teamcolor}!")
    if display == 1:
        displaytext(f"{mode.upper()} POINT", 1)
        displaytext(f"{teamcolor.upper()}", 2)
    # Set new color for the point
    set_color(teamcolor)

    if capture_self_reset == 1:
        capture_set_self_reset_when()
    send_message(
        f"<?xml version=1.0 encoding=UTF-8 ?><root><name>{name}</name><mode>{mode}</mode><color>{teamcolor}</color><startcolor>{start_color}</startcolor></root>")
    buzzer_cap_complete()
    print(f"Returning to looplife")
    time.sleep(5)


def sticky_key(buttoncolor):
    print(f"{buttoncolor} button is stuck!")
    displaytext(f"STICKY KEY!", 1)
    displaytext(f"{buttoncolor.upper()} STUCK!", 2)
    if has_buzzer == 1:
        for i in range(5):
            bz.on()
            time.sleep(0.1)
            bz.off()
            time.sleep(0.2)
    time.sleep(1)


def capture_time_check(button, buttoncolor):
    while button.is_held:
        try:
            if button.held_time < capture_time:
                displaytext(f"Capturing: ({math.trunc(capture_time - button.held_time)})", 2)
            if button.held_time > 1.5 * capture_time:
                print(f"The {buttoncolor} is stuck or someone is being slow on purpose")
                sticky_key(buttoncolor)
                return
            if button.held_time > capture_time:
                print(f"Capture completed by {buttoncolor}, held for {button.held_time}.")
                capture_complete(buttoncolor)
        except:
            displaytext(f"{mode.upper()} POINT", 1)
            displaytext(f"Aborted", 2)
            time.sleep(1)


def point_refresh():
    print(f"Refreshing point {name.upper()}")
    send_message(f"<?xml version=1.0 encoding=UTF-8 ?><root><name>{name}</name><mode>{mode}</mode><color>{color}</color><startcolor>{start_color}</startcolor></root>")

    # Display info
    displaytext(f"Refreshed point", 1)
    displaytext(f"{name}", 2)
    time.sleep(2)
    # Return the global
    global point_refresh_time
    point_refresh_time = time.time()
    return spawn_last_spam


# Be cool and show off
def tecpinfo():
    displaytext("TECP 0.03", 1)
    displaytext("ASN-TAK", 2)
    time.sleep(2)


# send initial state
def send_initial_state():
    print(f"Sending initial state of the point:")
    displaystatus()
    print(
        f"<?xml version=1.0 encoding=UTF-8 ?><root><name>{name}</name><mode>{mode}</mode><color>{color}</color><startcolor>{start_color}</startcolor></root>")
    send_message(
        f"<?xml version=1.0 encoding=UTF-8 ?><root><name>{name}</name><mode>{mode}</mode><color>{color}</color><startcolor>{start_color}</startcolor></root>")
    print(f"Initial message sent")


def displaystatus():
    displaytext(f"{mode.upper()} POINT", 1)
    displaytext(f"{color.upper()}", 2)


# Show tecp version

tecpinfo()

# Sending initial state from config.json

send_initial_state()

# loop forever
print(f"Starting looping forever")

while True:

    # Resets after x time if self_reset is enabled.
    if capture_self_reset == 1 and mode == "capture":
        if capture_self_reset_when > time.time():
            capture_self_reset_triggered()

    # Spam spawn status at frequent intervals
    if mode == "spawn":
        if time.time() > spawn_last_spam + spawn_refresh_cycle * 60:
            spawn_refresh()
    # Check for button presses:
    if blue_button.is_active:
        capture_time_check(blue_button, "blue")
    if red_button.is_active:
        capture_time_check(red_button, "red")
    if yellow_button.is_active:
        capture_time_check(yellow_button, "yellow")

    # Check buzzer and spawn cycle buzzer is enabled
    if has_buzzer == 1:
        # Check if it's time to respawn.
        if mode == "spawn" and time.time() - spawn_cycle_timer_start >= spawn_main_cycle * 60:
            buzzer_spawn_cycle()
        if mode == "rally" and time.time() - spawn_cycle_timer_start >= spawn_rally_cycle * 60:
            buzzer_spawn_cycle()
    # Refresh point so the marker does not go stale
    if time.time() >= point_refresh_time + (point_refresh_cycle * 60):
        point_refresh()

    # Refresh screen in case fuckery
    displaystatus()
    # sleep for a short amount of time to avoid consuming too much CPU
    time.sleep(0.2)
