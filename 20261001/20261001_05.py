from machine import Pin
import time

flash = Pin(4, Pin.OUT, value = 0)
red = Pin(33, Pin.OUT, value = 1)


led_blink = 0



def flash_on():
    flash.value(not flash.value())
    
def red_on():
    red.value(not red.value())

    
while led_blink < 20000:
    time.sleep_ms(1)
    led_blink += 1
          
    if led_blink % 500 == 0:
        flash_on()
    elif led_blink < 2000:
        flash_on()
    elif 2000 < led_blink < 6000:
        if led_blink % 1000 == 0:
            flash_on()
    elif led_blink > 6000:
        if led_blink % 5000 == 0:
            flash_on()
    else:
        flash.value(0)
    
    
    if led_blink % 500 == 0:
        red_on()
    else:
        red.value(1)
    
        
flash.value(0)
red.value(1)        
    

