from machine import Pin
import time

red = Pin(33, Pin.OUT, value=1)

def S():
    red.value(0)
    time.sleep_ms(300)
    red.value(1)
    time.sleep_ms(50)
    
def O():
    red.value(0)
    time.sleep_ms(900)
    red.value(1)
    time.sleep_ms(50)
    
def T():
    red.value(0)
    time.sleep_ms(50)
    red.value(1)
    time.sleep_ms(50)
    
def A():
    red.value(0)
    time.sleep_ms(1000)
    red.value(1)
    time.sleep_ms(500)
    
count = 1
while count < 4:
    print("SOS", count)
    count += 1
    S()
    S()
    S()
    O()
    O()
    O()
    S()
    S()
    S()
while 2 < count < 9:
    print("TA", count)
    count += 1
    T()
    T()
    A()
    A()
while count > 7:
    count = 0
    print("END", count)