import network, time, ntptime
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan() # Scan for available access points
sta_if.connect("VG3Data", "Admin:1234") # Connect to an AP
while not sta_if.isconnected():
    time.sleep(0.1)
print(sta_if.ifconfig())

print("Local time before synchronization：%s" %str(time.localtime()))
# Denne funksjonen henter dato og tid fra internet. Tidsone UTC
# https://no.wikipedia.org/wiki/Network_Time_Protocol
# https://mpython.readthedocs.io/en/latest/library/micropython/ntptime.html

ntptime.settime()
print("Local time after synchronization：%s" %str(time.localtime()))