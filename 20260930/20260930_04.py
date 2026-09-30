from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

counter = 0
red_on = 0

a = 10
b = 1

while a > b :
    flash.value(1)
    if(red_on == 1) :
        red.value(0)
    time.sleep_ms(500)
    
    flash.value(0)
    if(red_on == 1) :
        red.value(1)
        red_on = 0
    time.sleep_ms(500)
    
    counter += 1
    b += 1
    if counter > 2 :
        counter = 0
        red_on = 1
