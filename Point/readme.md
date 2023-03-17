```
     ______   ______   ______   ____ 
    /_  __/  / ____/  / ____/  / __ \
     / /    / __/    / /      / /_/ /
    / /    / /___   / /___   / ____/ 
   /_/    /_____/   \____/  /_/      
```         
# TECP Point script
When running in cojunction with a meshtastic device will publish default information based on `config.json` and will change color based on GPIO buttons. 

Meshtastic device must have serial enabled. 
```meshtastic --set serial.enabled true ```

Default GPIO pins are for colors are:

* Red
  * GPIO 17
* Blue
  * GPIO 22
* Yellow
  * GPIO 27
* Buzzer
  * GPIO 23

On power off or restart of script it will revert to config.json 

Parts:
* Buzzer
  * https://www.aliexpress.com/item/4000100829835.html
* Buttons
  * https://www.aliexpress.com/item/1005004710768369.html
  
# Components

![image](https://user-images.githubusercontent.com/25975089/226065087-a6517b9e-0c47-4071-94a2-ff081d562e71.png)

[Meshtastic](https://meshtastic.org/) devices used to create the mesh network.

Single board computer, like a raspberry pi zero, bananapi or whatever you have readily access to.



