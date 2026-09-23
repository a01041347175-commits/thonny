from machine import Pin
import time

flash = 4
red_led = 33

def blink_once(pin_no, times, ms_on, ms_off):

    if pin_no == red_led :
        ON = 0
        OFF = 1
    else :
        ON = 1
        OFF = 0
        
    led_controller = Pin(pin_no, Pin.OUT, value=0)
    for i in range(times) :
        led_controller.value(ON)
        time.sleep_ms(ms_on)
        led_controller.value(OFF)
        time.sleep_ms(ms_off)
    
blink_once(4, 3, 300, 500)
blink_once(33, 3, 100, 500)