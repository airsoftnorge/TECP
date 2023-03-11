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

* gateway.py
  * Route meshtastic events into node-red for proccessing and distribution
* flows.json
  * Contains the flows required for node-red to understand meshtastic events received by the gateway