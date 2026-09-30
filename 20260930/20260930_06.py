from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

a = 10

for b in range(1, a):
    flash.value(1)
    time.sleep_ms(1000)
    if b % 3 == 0:
        time.sleep_ms(900)
        red.value(0)
        time.sleep_ms(100)
        red.value(1)
        flag_red = 0
        
    else :
        time.sleep_ms(1000)
    
    flash.value(0)
    time.sleep_ms(1000)