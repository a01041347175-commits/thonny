from machine import Pin
import time

red = Pin(33, Pin.OUT, value = 0)

for i in range(3):
    def A(a):
        red.value(0)
        time.sleep_ms(a)
        red.value(1)
        time.sleep_ms(a)
    
    A(1000)
    A(500)