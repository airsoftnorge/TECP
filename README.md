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

Points will be displayed using mil-std-2525 icons. 

Friendly points are displayed as cyan rectangles:  ![image](https://user-images.githubusercontent.com/25975089/224482967-b65e6aac-3ea6-467e-b414-f8c413cf2214.png)

Enemy points are displayed as red diamons:  ![image](https://user-images.githubusercontent.com/25975089/224482983-6dd2923c-d575-45b1-a8a7-a7d7c0ee4f93.png)

Neutral points are displayed as green squares:  ![image](https://user-images.githubusercontent.com/25975089/224482953-7fca8f3f-d7ec-4c12-94e5-75ae2af6f6b8.png)

### Mode: Capture
Capturable points by holding down a button for a configurable amount of time. Upon capture the status will be broadcast on meshtastic to the gateway, updating the TAK servers.



### Mode: Spawn
Non capturable points.



### Mode: Rally
Rally points are only seen to the color they are configured for, acts as a moveable spawn point.
Can be disabled by other team and must be re-enabled to work.


### How it should look when completed
![image](https://user-images.githubusercontent.com/25975089/224479390-c94bbf40-a6f5-4022-a651-db9e5723f404.png)
