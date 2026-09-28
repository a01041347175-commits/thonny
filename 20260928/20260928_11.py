from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

slow = [800, 800, 800]
fast = [100, 100, 100, 100, 100, 100]

for ms in slow:
    flash.value(1)
    time.sleep_ms(ms)
    flash.value(0)
    time.sleep_ms(200)
    
for ms in fast:
    flash.value(1)
    time.sleep_ms(ms)
    flash.value(0)
    time.sleep_ms(200)
    
def run_pattern(pin_obj, pattern_list):
    if pin_obj == red:
        ON = 0
        OFF = 1
    else:
        ON = 1
        OFF = 0
        
    for ms in pattern_list:
        pin_obj.value(ON)
        time.sleep_ms(ms)
        pin_obj.value(OFF)
        time.sleep_ms(ms)
        
run_pattern(red, slow)
run_pattern(red, fast)