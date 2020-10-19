# OM det kommer feil med socket i use
# skriv: machine.reset() i REPL

import net
import usocket as socket
import machine
import time

LED_PIN = 2

led = machine.Pin(LED_PIN, machine.Pin.OUT)

def index(led_state):
    header = 'HTTP/1.0 200 OK\r\nContet-Type: text/html; charset=utf-8\r\n\r\n'
    html = '''
    <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body>
        <h1>Dette er den fine led statusen: {}</h1>
        <a href="?led=on"><button>ON</button><br>
        <a href="?led=off"><button>OFF</button><br>
        </body>
    </html>
    '''.format(led_state)
    return header + html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
try:
    while True:
        conn, addr = s.accept()
        print('Got a connection from: ', str(addr))
        request = conn.recv(1024)
        print(request[:50])
        lv = led.value()
        if 'led=off' in request:
            lv = 0
        if 'led=on' in request:
            lv = 1

        time.sleep_ms(1)

        led.value(lv)
        print(lv)
        response = index(lv)
        conn.send(response)
        conn.close()
finally:
    s.close()









