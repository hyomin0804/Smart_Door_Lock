import RPi.GPIO as GPIO
from lcd import *

def led2_clean():

    led_pins = [18, 19, 21]
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(led_pins[0], GPIO.OUT)
    GPIO.setup(led_pins[1], GPIO.OUT)
    GPIO.setup(led_pins[2], GPIO.OUT)

    GPIO.cleanup()
    lcd_clear()

#led2_clean()
