from machine import Pin,PWM
from random import randint
import time

pins = [15,2,0]

pwm_r = PWM(Pin(pins[0]), 10000)
pwm_g = PWM(Pin(pins[1]), 10000)
pwm_b = PWM(Pin(pins[2]), 10000)

def setColor(r, g, b):
    pwm_r.duty(1023-r)
    pwm_g.duty(1023-g)
    pwm_b.duty(1023-b)

try:
    while True:
        red   = randint(0, 1023)
        green = randint(0, 1023)
        blue  = randint(0, 1023)
        setColor(red, green, blue)
        time.sleep_ms(200)
finally:
    pwm_r.deinit()
    pwm_g.deinit()
    pwm_b.deinit()

