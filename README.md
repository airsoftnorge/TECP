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
Each point contains a raspberry pi and a meshtastic device. Capture mode units will also contain a set of pushbuttons to interact with GPIO to let players capture them.


### Mode: Capture
Capturable points by holding down a button for a configurable amount of time. Upon capture the status will be broadcast on meshtastic to the gateway, updating the TAK servers.
Will be represended in TAK with mil-std-2525 icons matching the friendly/enemy/neutral status in relation to your team color. 


### Mode: Spawn
Non capturable points.
Will be represended in TAK with mil-std-2525 icons matching the friendly/enemy/neutral status in relation to your team color. 

### Mode: Rally
Rally points are only seen to the color they are configured for, acts as a moveable spawn point.
Can be disabled by other team and must be re-enabled to work.
Will be represended in TAK with mil-std-2525 icons

### How it should look when completed
![image](https://user-images.githubusercontent.com/25975089/224479390-c94bbf40-a6f5-4022-a651-db9e5723f404.png)
