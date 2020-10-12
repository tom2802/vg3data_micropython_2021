# Write your code here :-)
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
    # Tester knappen x antall ganger for at det skal være en stabil verdi
    for n in range(20):
        bv = btn.value()
        time.sleep_ms(1)
    led.value(not bv)
    time.sleep(0.1)
