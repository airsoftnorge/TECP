# TECP
**T**AK **E**nabled **C**apture **P**oint for airsoft games

# Idea
Have physical points of interest that can be captured and have them reflect which teams hold which points on their TAK EUD.

# Parts

## TAK Gateway
Responsible for bringing points and statuses of points from the meshtastic network to the TAK servers in a COT format.


Hardware: Raspberry pi, Meshtastic device, LTE USB dongle.

## Meshtastic enabled capture point
Responsible for sending team capture (red/blue) information to the tak gateway via the meshtastic network

Hardware: Raspberry pi, meshtastic device, momentary push buttons.

## Meshtastic enabled rally points
Responsible for sending rally point information over the meshtastic network.

Raspberry pi, meshtastic device

## Meshtastic enabled uncapturable spawn points
Responsible for sending spawn point information over the meshtastic network.

Raspberry pi, meshtastic device

# How it should look when completed
![image](https://user-images.githubusercontent.com/25975089/224479390-c94bbf40-a6f5-4022-a651-db9e5723f404.png)
