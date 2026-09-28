from machine import Pin
import time

flash = 4
red_led = 33

def print_word(pin_no, pin, ON, count):
    if pin_no == red_led:
        name = "red_led"
    elif pin_no == flash:
        name = "flash"
            
    if pin.value() == ON:
        print(name, "ON -", count, "회")
    else:
        print(name, "OFF")
        
def blink_once(pin_no, times, ms_on, ms_off):
    if pin_no == red_led:
        ON = 0
        OFF = 1
    else:
        ON = 1
        OFF = 0
        
    led_controller = Pin(pin_no, Pin.OUT, value=0)
    for i in range(times):
        led_controller.value(ON)
        print_word(pin_no, led_controller, ON, i+1)
        time.sleep_ms(ms_on)
        led_controller.value(OFF)
        print_word(pin_no, led_controller, ON, i+1)
        time.sleep_ms(ms_off)
        
blink_once(4, 5, 500, 500)
blink_once(33, 5, 1000, 1000)