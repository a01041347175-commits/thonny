from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)

UNIT = 150
iLoveYou = [1, 1, 0,       #I
            1, 3, 1, 1, 0, #L
            3, 3, 3, 0,    #O
            1, 1, 1, 3, 0, #V
            1, 0,          #E
            3, 1, 3, 3, 0, #Y
            3, 3, 3, 0,    #O
            1, 1, 3]       #U

def send_morse(pin_obj, signals, unit):
    for s in signals:
        pin_obj.value(1)
        time.sleep_ms(s*unit)
        pin_obj.value(0)
        time.sleep_ms(unit)
        
send_morse(flash, iLoveYou, UNIT)
print("I LOVE YOU 전송 완료")