import network, time
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.scan() # Scan for available access points
sta_if.connect("VG3Data", "Admin:1234") # Connect to an AP
while not sta_if.isconnected():
    time.sleep(0.1)
print(sta_if.ifconfig())
