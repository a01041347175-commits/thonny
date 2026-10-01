from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)


def pattern(count, number):
    for b in range(1, count + 1):
        flash.value(1)
        if b % number == 0:
            time.sleep_ms(900)
            red.value(0)
            time.sleep_ms(100)
            red.value(1)                
        else :
            time.sleep_ms(1000)
    
        flash.value(0)
        time.sleep_ms(1000)

pattern(9, 3)
pattern(10, 5)
