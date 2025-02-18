import gpiozero
import time
from signal import pause
from gpiozero import LED, Button

led = LED(17)
led.on()
time.sleep(2)
led.off()


RELAY_PIN1 = 16
RELAY_PIN2 = 20

door1 = gpiozero.OutputDevice(RELAY_PIN1, active_high=False, initial_value=False)
door2 = gpiozero.OutputDevice(RELAY_PIN2, active_high=False, initial_value=False)

door1.on()
time.sleep(2)
door1.off()

door2.on()
time.sleep(2)
door2.off()



button = Button(21)

def door_open():
    print("say dooropen!")
def door_close():
    print("say close!")


button.when_released = door_open
button.when_pressed = door_close

pause()


