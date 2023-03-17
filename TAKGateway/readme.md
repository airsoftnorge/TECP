```
     ______   ______   ______   ____ 
    /_  __/  / ____/  / ____/  / __ \
     / /    / __/    / /      / /_/ /
    / /    / /___   / /___   / ____/ 
   /_/    /_____/   \____/  /_/      
```         
# TECP Gateway

Meshtastic device must have serial enabled. 
```meshtastic --set serial.enabled true ```

# Setup options:
### Hosted
Capturepoints -> Gateway -> External MQTT -> Node-Red combines information needed -> Send COTs to the game TAK servers.
* Pro: Server is remotely accessible for game-admin purposes.
* Con: 4 dollars a month.
### Local
Capturepoints -> Gateway -> Internal MQTT -> Node-Red combines information needed -> Send COTs to the game TAK servers.
* Pro: Don't need another server.
* Con: cannot adjust anything without physical access.


# MQTT Server
![image](https://user-images.githubusercontent.com/25975089/226064820-406703e5-b2b7-421d-a944-83243b83fae8.png)

[Mosquitto](https://mosquitto.org/) [MQTT](https://en.wikipedia.org/wiki/MQTT) server, maintains the updates from each point.

You can setup by yourself or contact us for access if you want to utilize the public servers. 


# Node-Red
![image](https://user-images.githubusercontent.com/25975089/226064955-492a8955-0030-46c5-b2e9-caabe88e5c71.png)


[Node-Red](https://nodered.org/) feeds points from the MQTT into the TAK servers. 

Sorting for color, determining if the point is friendly, enemy or unknown based on server color. 

![image](https://user-images.githubusercontent.com/25975089/226060472-1ecdc5b5-f941-4188-abb2-31b723fafa18.png)

Getting location variables for input not yet decided upon. 
Might store info in a sqlite db if needed, unknown at this time. 
