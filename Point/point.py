#
#     ______   ______   ______   ____
#    /_  __/  / ____/  / ____/  / __ \
#     / /    / __/    / /      / /_/ /
#    / /    / /___   / /___   / ____/
#   /_/    /_____/   \____/  /_/
#
#


import json
import time

import meshtastic
import meshtastic.serial_interface

from gpiozero import Button
from gpiozero import Buzzer

from rpi_lcd import LCD

#Clean screen if something is still there:
lcd.clear()

# set up GPIO pins for buttons
bz = Buzzer(23)
red_button = Button(17, bounce_time=0.05)
blue_button = Button(22, bounce_time=0.05)
yellow_button = Button(27, bounce_time=0.05)

# Setup all default values, in case of partial configs.
name = ""
mode = ""
display = 0
start_color = ""
capture_time = 30
has_buzzer = 0
spawn_buzzer = 0
spawn_main_cycle = 30
spawn_rally_cycle = 15
spawn_cycle_timer = 0
spawn_cycle_timer_start = time.time()
color = start_color

capture_self_reset = 0
capture_self_reset_timer = 15
capture_self_reset_when = float(time.time() + 99999)

spawn_last_spam = time.time()
spawn_refresh_cycle = 2



# load the configuration data from the JSON file
with open("config.json", "r") as f:
    config_data = json.load(f)
    print("Loaded config:")
    print(config_data)

# Get keys from config
for key, value in config_data.items():
    globals()[key] = value


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
        for i in range(5):
            bz.on()
            print(f"BEEP")
            time.sleep(0.25)
            bz.off()
            time.sleep(0.25)


def buzzer_spawn_cycle():
    global spawn_cycle_timer_start
    print(f"Time for a {mode} respawn!")
    for i in range(3):
        bz.on()
        print(f"BEEP")
        time.sleep(1)
        bz.off()
        time.sleep(0.25)
    print(f"Resetting spawn cycle!")
    spawn_cycle_timer_start = time.time()
    return spawn_cycle_timer_start


# send initial state

def send_initial_state():
    print(f"Sending initial state of the point")
    send_message(f"<?xml version=1.0 encoding=UTF-8 ?><root><name>{name}</name><mode>{mode}</mode><color>{color}</color><startcolor>{start_color}</startcolor></root>")
    print(f"Initial message sent")


# Sending initial state from config.json
send_initial_state()


def capture_complete(color):
    print(f"Point {name} has been captured by {color}!")
    if capture_self_reset == 1:
        capture_set_self_reset_when()
    send_message(f"<?xml version=1.0 encoding=UTF-8 ?><root><name>{name}</name><mode>{mode}</mode><color>{color}</color><startcolor>{start_color}</startcolor></root>")
    buzzer_cap_complete()
    print(f"Returning to looplife")
    time.sleep(5)
    return (color)

def printlcd(text:str,num:int):
    if display == 1:
        lcd.text(text, num)
        time.sleep(0.25)




def capture_time_check(button, color):
    if button.is_held:
        if button.held_time < float(1):
            print(f"Capture attempt started by {color}.Capture time is {capture_time} seconds")
        if button.held_time > 1.5 * capture_time:
            print(f"Release the button, you've held it for {button.held_time} already and triggered a win!")
        if button.held_time > capture_time:
            print(f"Capture completed by {color}, held for {button.held_time}.")
            capture_complete(color)


def spawn_refresh():
    print(f"Refreshing {start_color} spawn {name}")
    capture_complete(start_color)
    spawn_last_spam = time.time()
    return spawn_last_spam


# loop forever
print(f"Starting looping forever")

while True:
    # Resets after x time if self_reset is enabled.
    if capture_self_reset == 1 and mode == "capture":
        if capture_self_reset_when > time.time():
            capture_self_reset_triggered()

    # Spam spawn status at frequent intervals
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
    if spawn_buzzer == 1 and has_buzzer == 1:
        # Check if it's time to respawn.
        if mode == "spawn" and time.time() - spawn_cycle_timer_start >= spawn_main_cycle * 60:
            buzzer_spawn_cycle()
        if mode == "rally" and time.time() - spawn_cycle_timer_start >= spawn_rally_cycle * 60:
            buzzer_spawn_cycle()

    # sleep for a short amount of time to avoid consuming too much CPU
    time.sleep(0.1)
