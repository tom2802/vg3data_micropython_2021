from machine import TouchPad, Pin
from time import sleep_ms
p = Pin(4) # Oppretter en instans av en Pin
t = TouchPad(p) # Oppretter en instans av TouchPad, denne tar en pinne instans som parameter
t.read() # Leser verdien. Denne returnerer en analog verdi. Verdien er mindre når det er kontakt

# Leser verdier i en løkke
while True:
    print(t.read())
    sleep_ms(500)
