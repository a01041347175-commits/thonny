from machine import Pin
import time

red = Pin(33, Pin.OUT, value=1)


def blink_once():
    red.value(0)
    time.sleep_ms(300)
    red.value(1)
    time.sleep_ms(100)
    
def blink_twice():
    red.value(0)
    time.sleep_ms(900)
    red.value(1)
    time.sleep_ms(100)
    
def blink_0():
    red.value(0)
    time.sleep_ms(50)
    red.value(1)
    time.sleep_ms(50)

for i in range(2):
    blink_once()
    blink_once()
    blink_once()
    blink_twice()
    blink_twice()
    blink_twice()
    blink_once()
    blink_once()
    blink_once()
    blink_0()
    blink_0()
    blink_0()
    blink_0()