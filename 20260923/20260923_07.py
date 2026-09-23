from machine import Pin
import time

red = Pin(33, Pin.OUT, value = 0) #여러 문법을 섞어서 사용시 들여쓰기 중요#

def A(a):
    for i in range(3):
        red.value(0)
        time.sleep_ms(a)
        red.value(1)
        time.sleep_ms(a)
    
A(1000)
A(500)
