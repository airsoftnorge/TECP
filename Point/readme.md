```
     ______   ______   ______   ____ 
    /_  __/  / ____/  / ____/  / __ \
     / /    / __/    / /      / /_/ /
    / /    / /___   / /___   / ____/ 
   /_/    /_____/   \____/  /_/      
```         
# TECP Point script
When running in conjunction with a meshtastic device will publish default information based on `config.json` and will change color based on GPIO buttons. 

Meshtastic device must have serial enabled. 
```meshtastic --set serial.enabled true ```

#### Pins are assumed in the program to match the following:

* Red button +
  * GPIO 17 (Pin 11)
* Blue button + 
  * GPIO 22 (Pin 15)
* Yellow button +
  * GPIO 27 (Pin 13)
* Buzzer +
  * GPIO 23 (Pin 16)
* 1602 display
  * GPIO 02 (Pin 3) - SDB
  * GPIO 03 (Pin 5) - SDA
  * GPIO 5v (Pin 4) - VCC
  * GPIO GND (Pin 6) - GND
    
Reference for pins:

![image](https://user-images.githubusercontent.com/25975089/230800721-6f9b2a26-ac37-4fce-bc4b-4ee5b8916710.png)


On power off or restart of script it will revert to config.json 


# Example build list:
* Pi Zero with headers
  * https://raspberrypi.dk/en/product/raspberry-pi-zero-wh-with-pre-soldered-header/
* Meshtastic device
  * https://www.lilygo.cc/products/t-beam-v1-1-esp32-lora-module?variant=42204034990261
* Build case
  * https://www.planostore.com/plano-shot-shell-box-od-green
* Buzzer
  * https://www.aliexpress.com/item/4000100829835.html
* Buttons
  * https://www.aliexpress.com/item/1005004710768369.html
* Screen
  * https://www.aliexpress.com/item/1005001941636245.html

All parts here are interchangible with any simmilar part, button is a button, any single board computer will do the trick. Banana Pi is probably a much easier device to get a hold of multiple at once. Screen and buzzer is optional and you can build in whatever case you so desire. 
  
# Components

![image](https://user-images.githubusercontent.com/25975089/226065087-a6517b9e-0c47-4071-94a2-ff081d562e71.png)

[Meshtastic](https://meshtastic.org/) devices used to create the mesh network.

Single board computer, like a raspberry pi zero, bananapi or whatever you have readily access to.



