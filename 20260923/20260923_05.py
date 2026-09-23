from machine import Pin
import time

red = Pin(33, Pin.OUT, value = 0)

def blink(a):
    red.value(0)
    time.sleep_ms(a)
    red.value(1)
    time.sleep_ms(a)
    
for i in range(3):
    blink(1000)
    blink(100)
    
    