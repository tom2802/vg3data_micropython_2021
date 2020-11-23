from machine import Pin
import time

sensor_pin = Pin(14,Pin.IN)
led_pin = Pin(2,Pin.OUT)

try:
    while True:
      if not sensor_pin.value():     
        led_pin.value(1)  #Set led turn on
      else:
        led_pin.value(0)  #Set led turn of
except:
    pass
