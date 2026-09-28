from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
patterns = [300, 100, 600, 100, 300]

patterns[2] = 900
print(len(patterns))
print(patterns)
#매개변수 추가 append

patterns.append(900)
print(len(patterns))
print(patterns)

patterns.append(1000)
print(len(patterns))
print(patterns)

for ms in patterns:
    print("이번 곡:", ms)
    flash.value(1)
    time.sleep_ms(ms)
    flash.value(0)
    time.sleep_ms(150)
    
print("끝")