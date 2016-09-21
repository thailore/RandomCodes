#---------------------------------------------------
#Tylor Borgeson
#
#Purpose: UDP_Server Ping Program
#         Assignment 4 Networks
#         Generate random lost packets
#---------------------------------------------------

import random
from socket import *

def main():
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', 12000))

    while True:
        rand = random.randint(0, 10)
        message, address = serverSocket.recvfrom(1024)
        message = message.upper()
        if rand < 4:
            continue
        serverSocket.sendto(message, address)

    pass

if __name__ == '__main__':
    main()
