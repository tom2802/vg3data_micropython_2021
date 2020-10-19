# Write your code here :-)
# Maks venstre = 135
# Maks høyre = 20

from machine import PWM, Pin
import time
servo = PWM(Pin(15), freq=50, duty=87)
while True:
    time.sleep(1)
    servo.duty(20)
    time.sleep(1)
    servo.duty(135)
