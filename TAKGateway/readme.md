```
     ______   ______   ______   ____ 
    /_  __/  / ____/  / ____/  / __ \
     / /    / __/    / /      / /_/ /
    / /    / /___   / /___   / ____/ 
   /_/    /_____/   \____/  /_/      
```         
# TECP Gateway

Meshtastic gateway is just a normal point, it requires a internet connection. You can use this as a normal capture point or a dedicated gateway in the mode settings for the point.

Meshtastic device must have serial enabled and echo back:

```meshtastic --set serial.enabled true --set serial.echo true```

Meshtastic gateway device must be on the correct channel and have uplink enabled:

```meshtastic --ch-set name ASN --ch-index 0 --ch-set channel_num 1 --ch-index 0 --ch-set psk <PSK> --ch-medfast --set lora.region EU_868 --set serial.enabled true --ch-set uplink_enabled true```

Must also have MQTT enabled to push points to our or your own mqtt server for processing and shipping to each server:

```meshtastic --set mqtt.enabled true --set mqtt.jsonEnabnled true --set mqtt.address mqtt.airsoftnorge.com:1883 --set mqtt.username "<your username>" --set mqtt.password "<your password>" ```

# Setup options:

### ASN-TAK Infrastructure
Capturepoints -> Meshtastic -> Gateway -> ASN-MQTT Server
* Pro: Don't have to configure anything custom or setup node-red or mqtt yourself
* Con: You might want things to behave differently.
Contact us on [discord](https://discord.gg/m3yaCJWtAk) for access if you want to utilize the ASN-TAK servers. 

### Self hosted
Capturepoints -> Meshtastic -> Gateway -> External MQTT -> Node-Red combines information needed -> Send COTs to the game TAK servers.
* Pro: Server is remotely accessible for game-admin purposes.
* Con: 4 dollars a month.
 
### Local
Capturepoints -> Meshtastic -> Gateway -> Internal MQTT -> Node-Red combines information needed -> Send COTs to the game TAK servers.
* Pro: Don't need another server.
* Con: cannot adjust anything without physical access.


# MQTT Server
![image](https://user-images.githubusercontent.com/25975089/226064820-406703e5-b2b7-421d-a944-83243b83fae8.png)

[Mosquitto](https://mosquitto.org/) [MQTT](https://en.wikipedia.org/wiki/MQTT) server, maintains the updates from each point.

You can setup your own or contact us on [discord](https://discord.gg/m3yaCJWtAk) for access if you want to utilize the ASN-TAK servers. 


# Node-Red
![image](https://user-images.githubusercontent.com/25975089/226064955-492a8955-0030-46c5-b2e9-caabe88e5c71.png)

[Node-Red](https://nodered.org/) feeds points from the MQTT into the TAK servers. 

Sorting for color, determining if the point is friendly, enemy or unknown based on server color. 

![image](https://user-images.githubusercontent.com/25975089/230047472-9fe03f09-921d-4594-9074-277304cbab70.png)
