from machine import Pin
import time

red = Pin(33, Pin.OUT, value = 0)

def blink(msg):#함수 이름 괄호안에 내용을 임의로 설정을하면 함수 실행시 편하다#
    red.value(0)
    time.sleep_ms(msg)
    red.value(1)
    time.sleep_ms(msg)
    
count = 0
while count < 2:
    count += 1
    print("END", count)
    blink(1000)
    blink(500)
    blink(1000)
    blink(500)