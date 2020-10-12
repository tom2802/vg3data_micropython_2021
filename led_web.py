import net
import usocket as socket
import machine

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
        <h1>Dette er den fine led statusen: {}
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

        response = index('Led status')
        conn.send(response)
        conn.close()
finally:
    s.close()









