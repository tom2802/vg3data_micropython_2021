from machine import Pin,PWM
import time

pins=[15,2,0];

pwm_r = PWM(Pin(pins[0]), 1000)
pwm_g = PWM(Pin(pins[1]), 1000)
pwm_b = PWM(Pin(pins[2]), 1000)

def set_color(rgb):
    pwm_r.duty(1023-(rgb>>20))
    pwm_g.duty(1023-(rgb>>10))
    pwm_b.duty(1023-(rgb>>0))

def wheel(pos):
    wheel_pos = pos % 1023
    if wheel_pos < 341:
        return (((1023-wheel_pos*3)<<20)|((wheel_pos*3)<<10))
    elif wheel_pos >= 341 and wheel_pos < 682:
        wheel_pos -= 341
        return (((1023-wheel_pos*3)<<10)|(wheel_pos*3))
    else :
        wheel_pos -= 682;
        return (((wheel_pos*3)<<20)|(1023-wheel_pos*3))

try:
    while True:
        for i in range(0, 1023):
            set_color(wheel(i))
            time.sleep_ms(5)
finally:
    pwm_r.deinit()
    pwm_g.deinit()
    pwm_b.deinit()
