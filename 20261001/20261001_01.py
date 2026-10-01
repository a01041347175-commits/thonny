from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

while True:
    flash.value(1)
    time.sleep_ms(100)
    flash.value(0)
    time.sleep_ms(100)