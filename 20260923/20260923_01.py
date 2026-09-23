from machine import Pin
import time

red = Pin(33, Pin.OUT, value=1)

def S():
    red.value(0)
    time.sleep_ms(300)
    red.value(1)
    time.sleep_ms(50)

for i in range(3):
    S()
    S()
    S()
    
for i in range(1):
    print("END")