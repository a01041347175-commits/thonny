from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
patterns = [300, 300, 600,
    300, 300, 600,
    300, 300, 300, 300,
    700]

for ms in patterns:
    print("이번 곡:", ms)
    flash.value(1)
    time.sleep_ms(ms)
    flash.value(0)
    time.sleep_ms(150)
    
print("끝")