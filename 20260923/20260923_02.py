from machine import Pin
import time

red = Pin(33, Pin.OUT, value=1)

def NO_1():
    red.value(0)
    time.sleep_ms(1200)
    red.value(1)
    time.sleep_ms(500)
    red.value(0)
    time.sleep_ms(30)
    
def NO_2():
    red.value(0)
    time.sleep_ms(50)
    red.value(10)
    time.sleep_ms(50)

count = 0
while count < 8:
    count += 1
    print("Number", count)
    NO_1()
    NO_1()
    NO_2()
    NO_2()
    NO_2()
    NO_2()
    NO_2()
    
while count > 7:
    count = 0
    print("END")