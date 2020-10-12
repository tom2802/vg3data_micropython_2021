# Kobler en bryter mellom Pinne 12 og jord
import machine
import time

LED_PIN = 2
BTN_PIN = 13

#Instans av Led
led = machine.Pin(LED_PIN, machine.Pin.OUT)

# Instans av bryter
btn = machine.Pin(BTN_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

# Kjører en løkke for å teste
while True:
    led.value(not btn.value())
    time.sleep(0.1)
