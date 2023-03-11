```
     ______   ______   ______   ____ 
    /_  __/  / ____/  / ____/  / __ \
     / /    / __/    / /      / /_/ /
    / /    / /___   / /___   / ____/ 
   /_/    /_____/   \____/  /_/      
```         
# TECP Point script
When running in cojunction with a meshtastic device will publish default information based on `config.json` and will change color based on GPIO buttons. 
Default GPIO pins are for colors are:

* Red
  * GPIO 17
* Blue
  * GPIO 22
* Yellow
  * GPIO 27
* Buzzer
  * GPIO 23
  * 
On power off or restart of script it will revert to config.json 


Parts:
* Buzzer
  * https://www.aliexpress.com/item/4000100829835.html
* Buttons
  * https://www.aliexpress.com/item/1005004710768369.html