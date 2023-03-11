# TECP 
**T**AK **E**nabled **C**apture **P**oints for airsoft games

# Idea
Have physical points of interest that can be captured and have them reflect which teams hold which points on their TAK EUD.
Make the programming as easy to modify as possible, to enable new ideas to quickly be implemented. 

Implementation with [meshtastic](https://meshtastic.org/) to reduce cost of each unit.

# Moving parts

## TAK Gateway 

Responsible for bringing points and statuses of points from the meshtastic network to the TAK servers in a COT format.
Differentiate between rally points, spawns and capture points. 

TAKGateway displayed as neutral yellow: ![image](https://user-images.githubusercontent.com/25975089/224485693-f3db8eb4-2391-4e09-8fe6-65e82d45aef3.png)

Hardware: Raspberry pi, Meshtastic device, LTE USB dongle.

## Points
Each point contains a raspberry pi and a meshtastic device. Capture mode units will also contain a set of pushbuttons to interact with GPIO to let players capture them.

Points will be displayed using mil-std-2525 icons. 

Friendly points are displayed as cyan rectangles:  ![image](https://user-images.githubusercontent.com/25975089/224482967-b65e6aac-3ea6-467e-b414-f8c413cf2214.png)

Enemy points are displayed as red diamonds:  ![image](https://user-images.githubusercontent.com/25975089/224482983-6dd2923c-d575-45b1-a8a7-a7d7c0ee4f93.png)

Neutral points are displayed as green squares:  ![image](https://user-images.githubusercontent.com/25975089/224482953-7fca8f3f-d7ec-4c12-94e5-75ae2af6f6b8.png)

### Mode: Capture
Capturable points by holding down a button for a configurable amount of time. Upon capture the status will be broadcast on meshtastic to the gateway, updating the TAK servers.

### Mode: Spawn
Non-capturable points.


### Mode: Rally
Rally points are only seen to the color they are configured for, acts as a moveable spawn point for one side.
Can be disabled by other team if found and must be re-enabled to work.


### How it should look when completed
Friendly is always cyan, enemy is always red, neutral is always green and unknown is always yellow.

![image](https://user-images.githubusercontent.com/25975089/224486605-3f302c59-90d2-4e8f-8ee8-0d4645be5006.png)
* Friendly players in this map:
  * All cyan dots are friendly players. 
* Capture points in this map:
  * Alpha, Bravo, Charlie held by your team
  * Delta is neutral.
  * Echo and Foxtrot is held by the enemy team.
* Rally point:
  * Friendly rally point visible.
  * Enemy rally point not visible.
* Spawns:
  * Both spawns are visible to both teams.
* TAK Gateway:
  * Displyed as yellow.

