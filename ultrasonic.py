from machine import Pin
import time

trig_pin=Pin(13,Pin.OUT,0)
echo_pin=Pin(14,Pin.IN,0)

sound_velocity=340
distance=0

def get_sonar():
    trig_pin.value(1)
    time.sleep_us(10)
    trig_pin.value(0)
    while not echo_pin.value():
        pass
    ping_start=time.ticks_us()
    while echo_pin.value():
        pass
    ping_stop=time.ticks_us()
    ping_time=time.ticks_diff(ping_stop,ping_start)
    distance=ping_time*sound_velocity//2//10000
    return int(distance)

time.sleep_ms(2000)
while True:
    time.sleep_ms(500)
    print('Distance: ',get_sonar(),'cm' )
    
    
    
    
    
    
    
    
    
    
    
    
    