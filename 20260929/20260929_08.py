from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

def run_pattern(pin_obj, pattern_list, on=1):
    on = 1 if on else 0
    off = 1 - on
    for ms in pattern_list:
        pin_obj.value(on)
        time.sleep_ms(ms)
        pin_obj.value(off)
        time.sleep_ms(200)
        
def make_speedup(count, start, step):
    result = []
    for i in range(count):
        result.append(start - i*step)
    return result

pattern = make_speedup(20, 100, 5)
run_pattern(red, pattern, 0)