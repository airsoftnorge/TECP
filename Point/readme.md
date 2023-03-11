# TECP Point script
```
     ______   ______   ______   ____ 
    /_  __/  / ____/  / ____/  / __ \
     / /    / __/    / /      / /_/ /
    / /    / /___   / /___   / ____/ 
   /_/    /_____/   \____/  /_/      
```         
When running in cojunction with a meshtastic device will publish default information based on `config.json` and will change color based on GPIO buttons. 
Default GPIO pins are for colors are:

* Red
  * GPIO 17
* Blue
  * GPIO 22
* Yellow
  * GPIO 27

On power off or restart of script it will revert to config.json 
