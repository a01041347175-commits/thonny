from machine import Pin
import time



ON = 1
OFF = 0


def A(led, times, ms_on, ms_off):
    if led == 33:
        ON = 0
        OFF = 1
    else:
        ON = 1
        OFF = 0
    red = Pin(led, Pin.OUT, value=0)
    for i in range(times):
        red.value(ON)
        time.sleep_ms(ms_on)
        red.value(OFF)
        time.sleep_ms(ms_off)
    
A(4, 3, 1000, 100)
A(33, 3, 300, 1000)