# Pre-pre-pre-alpha
Do not use or try to make sense of.. public for sanity checking reasons. 

# **T**AK **E**nabled **C**apture **P**oints
```
     ______   ______   ______   ____ 
    /_  __/  / ____/  / ____/  / __ \
     / /    / __/    / /      / /_/ /
    / /    / /___   / /___   / ____/ 
   /_/    /_____/   \____/  /_/      
```                                  

# Idea
Have physical points of interest that can be captured and have them reflect which teams hold which points on their TAK EUD.
Make the programming as easy to modify as possible, to enable new ideas to quickly be implemented. 

# Features and anti-features 

At no point do you have to use your phone to interact with this. No QR-codes, no minigames within the game. Paper-map gang can have their fun. 

Implementation with [meshtastic](https://meshtastic.org/) to reduce cost of each unit.

Open source so you can take it and make something cooler if so desired. 

Everything here is preconfigured or made for [ASN-TAK](https://airsoftnorge.com/tak), if you intend to use it elsewhere you might need to make adjustments.
Contact us for MQTT login if you want to online your units on the ASN-TAK servers. 

We can be found ond [discord](https://discord.gg/m3yaCJWtAk) for any questions.

# Moving parts

## TAK Gateway 

Responsible for bringing points and statuses of points from the meshtastic network to the TAK servers in a COT format.
Differentiate between rally points, spawns and capture points. 

* TAKGateway displayed as neutral green: ![image](https://user-images.githubusercontent.com/25975089/226063791-ca2dff6c-61ee-4033-b3bf-3df42e37ee06.png)

Full configuration found [here](https://github.com/airsoftnorge/TECP/blob/main/TAKGateway/config.json)

## Points
Each point contains a raspberry pi and a meshtastic device. Capture mode units will also contain a set of push buttons to interact with GPIO to let players capture them.

Full configuration found [here](https://github.com/airsoftnorge/TECP/blob/main/Point/config.json)

* Points will be displayed using mil-std-2525 icons. 
* Friendly points are displayed as cyan rectangles:  ![image](https://user-images.githubusercontent.com/25975089/224482967-b65e6aac-3ea6-467e-b414-f8c413cf2214.png)
* Enemy points are displayed as red diamonds:  ![image](https://user-images.githubusercontent.com/25975089/224482983-6dd2923c-d575-45b1-a8a7-a7d7c0ee4f93.png)
* Unknown points are displayed as yellow blobs:  ![image](https://user-images.githubusercontent.com/25975089/226063905-da9f559a-fe30-4a10-8647-a31aa644e81a.png)


### Mode: Capture
Capturable points by holding down a button for a configurable amount of time. Upon capture the status will be broadcast on meshtastic to the gateway, updating the TAK servers.

Modifiers:
* Customizable capture time.
* Optional buzzer for audible capture.
* Permanent capture (default).
* Self resetting to initial color after a set amount of time.


### Mode: Spawn
Non-capturable points.

Modifiers:
* Optional buzzer for audible respawn alert.
* Custom rally respawn time (Only makes sense with a buzzer).

### Mode: Rally
Rally points are only seen to the color they are configured for, acts as a moveable spawn point for one side.
Can be disabled by other team if found and must be re-enabled to work.

Modifiers:
* Customizable deactivation time.
* Optional buzzer for audible respawn alert and deactivation alert.
* Custom rally respawn time (Only makes sense with a buzzer).


# Ideas for future expansion

* Optional: Have points revert to initial state after a set amount of time ✔️
* Optional: Support 16x2 LCD display giving you the state of the point. 
* Activate spawn points based on currently owned points.
* Force capture order


# How we expect it to look once done
Friendly is always cyan, enemy is always red, neutral is always green and unknown is always yellow.

![image](https://user-images.githubusercontent.com/25975089/226100329-8f1fd189-8a1e-42dc-b367-1ef818c3bf21.png)
* Friendly players in this map:
  * All cyan dots are friendly players. 
* Capture points in this map:
  * Alpha and Bravo is held by your team
  * Charlie and Delta is unknown.
  * Echo and Foxtrot is held by the enemy team.
* Rally point:
  * Friendly rally point visible.
  * Enemy rally point not visible.
* Spawns:
  * Both spawns are visible to both teams.
* TAK Gateway:
  * Displyed as green emplacement.

### Current iconography:
![image](https://user-images.githubusercontent.com/25975089/226099443-4faafd48-147a-4c48-894b-2f4fcaa18a2d.png)


