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

Capturepoints -> Gateway -> External MQTT -> Each server pulls from MQTT and create its own COTS -> Push to local taky server.

Capturepoints -> Gateway -> Internal MQTT -> Internal node-red create COTs ->  Push to red/blue 


# Node-Red
Feeds points from the MQTT into the TAK servers. 

![image](https://user-images.githubusercontent.com/25975089/226052181-d0dd69ff-c173-402b-9ea7-6a92ebd8e1ba.png)

Getting location variables for input not yet decided upon. 
Might store info in a sqlite db if needed, unknown at this time. 
