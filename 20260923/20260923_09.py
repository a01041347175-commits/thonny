from machine import Pin
import time

red = Pin(33, Pin.OUT, value=1)

ON = 0
OFF = 1

def print_word():
    if red.value() == ON:
        print("on")
    else:
        print("off")

def A(times, ms_on, ms_off):
    for i in range(times):
        red.value(ON)
        print_word()
        time.sleep_ms(ms_on)
        red.value(OFF)
        print_word()
        time.sleep_ms(ms_off)
    
A(3, 1000, 100)
A(10, 300, 1000)