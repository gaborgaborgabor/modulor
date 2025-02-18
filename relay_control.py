import gpiozero
import time
from signal import pause

RELAY_PIN = 16 #needs to connect to one of the relay pins

# to set from NC to open we need to init the pin with this parameter
relay = gpiozero.OutputDevice(RELAY_PIN, active_high=False, initial_value=False)


door = int(input('choose a door:'))

if door == 1:
    relay.on() #or off() for close
    


pause()