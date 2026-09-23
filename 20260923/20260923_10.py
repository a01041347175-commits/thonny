from machine import Pin
import time

red = Pin(33, Pin.OUT, value=1)

ON = 0
OFF = 1



def A(times, ms_on, ms_off):
    for i in range(times):
        red.value(ON)
        print("on", i + 1)
        time.sleep_ms(ms_on)
        red.value(OFF)
        print("off", i +1)
        time.sleep_ms(ms_off)
    
A(3, 1000, 100)
A(10, 300, 1000)