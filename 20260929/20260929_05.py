from machine import Pin
import time

flash = Pin(4, Pin.OUT, value=0)

UNIT = 150
ILOVEYOU = [1, 1, 0,
            1, 3, 1, 1, 0,
            3, 3, 3, 0,
            1, 1, 1, 3, 0,
            1, 0,
            3, 1, 3, 3, 0,
            3, 3, 3, 0,
            1, 1, 3]

def send_morse(pin_obj, signals, unit):
    for s in signals:
        pin_obj.value(1)
        time.sleep_ms(s*unit)
        pin_obj.value(0)
        time.sleep_ms(unit)
        
send_morse(flash, ILOVEYOU, UNIT)
print("I LOVE YOU 전송 완료")