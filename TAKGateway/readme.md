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


