import time
import machine
LED_PIN = 2

led = machine.Pin(LED_PIN, machine.Pin.OUT)
while True:
    led.value(not led.value())
    time.sleep(1)