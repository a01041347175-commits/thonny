from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)
red = Pin(33, Pin.OUT, value=1)

counter = 0
time_cnt = 0
red_on = 0

def timer_10ms():
    return

def timer_100ms():
    flash.value(not flash.value())
    
def timer_120ms():
    red.value(not red.value())
    
def timer_500ms():
    red.value(not red.value())

def timer_400ms():
    flash.value(not flash.value())

def timer_2000ms():
    flash.value(not flash.value())
    
while time_cnt < 10000:
    time.sleep_ms(1)
    time_cnt += 1
    
    if time_cnt % 400 == 0:
        timer_400ms()
    
    if time_cnt % 2000 == 0:
        timer_2000ms()
        
    if time_cnt % 120 == 0:
        timer_120ms()
        
    if time_cnt % 500 == 0:
        timer_500ms()

flash.value(0)
red.value(1)        
    