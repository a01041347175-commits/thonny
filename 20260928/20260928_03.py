from machine import Pin
import time

t0 = 300
t1 = 100
t2 = 600
t3 = 100
t4 = 300

flash = Pin(4, Pin.OUT, value=0)

flash.value(1);time.sleep_ms(t0);flash.value(0);time.sleep_ms(t3)