from machine import PWM, Pin, ADC
import time

adc = ADC(Pin(32))          # create ADC object on ADC pin
adc.atten(ADC.ATTN_11DB)    # set 11dB input attenuation (voltage range roughly 0.0v - 3.6v)
adc.width(ADC.WIDTH_10BIT)  # Resultat av lesingen vil bli 0 - 1023

pwm = PWM(Pin(2)) # Pin 2 er led på kortet
pwm.freq(10)
pwm.duty()
pwm.duty(128) # Duty er tiden pinnen er på 128/1023
pwm.duty(1023)

# Setter duty til verdien vi leser på adc (potensiometer)
while True:
    pwm.duty(adc.read())

