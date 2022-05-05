import time
from socket import socket,AF_INET, SOCK_DGRAM

s = socket(AF_INET, SOCK_DGRAM)
while(True):
    print(s.recv(8192))
    time.sleep(0.01)