#기본적으로 더 많이 사용하는 방법

from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

slow = [800, 800, 800]
fast = [100, 100, 100, 100, 100, 100]

def run_pattern(pin_obj, pattern_list, on):
    on = 1 if on else 0
    off = 1 - on
    for ms in pattern_list:
        pin_obj.value(on)
        time.sleep_ms(ms)
        pin_obj.value(off)
        time.sleep_ms(200)

run_pattern(flash, slow, 1)
run_pattern(red, fast, 0)