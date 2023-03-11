# TECP 
**T**AK **E**nabled **C**apture **P**oint for airsoft games

# Idea
Have physical points of interest that can be captured and have them reflect which teams hold which points on their TAK EUD.
Make the programming as easy to modify as possible, to enable new ideas to quickly be implemented. 

Implementation with [meshtastic](https://meshtastic.org/) to reduce cost of each unit.
Modelled after Squad 

# Moving parts

## TAK Gateway
Responsible for bringing points and statuses of points from the meshtastic network to the TAK servers in a COT format.
Differentiate between rally points, spawns and capture points. 

Hardware: Raspberry pi, Meshtastic device, LTE USB dongle.

## Points

### Mode: Capture points
Responsible for sending team capture (red/blue) information to the tak gateway via the meshtastic network
Hardware buttons when pressed over X time changes the color of the point, which is then sent over meshtastic to the gateway.

Hardware: Raspberry pi, meshtastic device, momentary push buttons.

### Mode: Spawn points
Responsible for sending spawn point information over the meshtastic network.
Same as the capture points but predefined color and no capture mechanism.

Raspberry pi, meshtastic device

### Mode: Rally points
Responsible for sending rally point information over the meshtastic network.
THis point will only be shown on the appropriate server, blue on blue and red on red. 

Raspberry pi, meshtastic device

### How it should look when completed
![image](https://user-images.githubusercontent.com/25975089/224479390-c94bbf40-a6f5-4022-a651-db9e5723f404.png)
