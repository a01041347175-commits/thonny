from machine import Pin
import time

def run_pattern(pin_obj, pattern_list):
    for ms in pattern_list:
        pin_obj.value(1)
        time.sleep_ms(ms)
        pin_obj.value(0)
        time.sleep_ms(200)
        
slow = [800, 800, 800]
fast = [100, 100, 100, 100, 100, 100]


run_pattern(flash, slow)
run_pattern(flash, fast)