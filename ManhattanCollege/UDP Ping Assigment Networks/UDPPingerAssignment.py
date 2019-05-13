#---------------------------------------------------
#Tylor Borgeson
#
#Purpose: UDP_Client Ping Program
#         Assignment 4 Networks
#         Send 10 Ping messages to target over UDP.
#         Determine and print RTT for each message
#---------------------------------------------------

#imports
from datetime import datetime
from socket import *

def main():
    serverName = 'localhost'
    serverPort = 12000 #port number from server program
    clientSocket = socket(AF_INET, SOCK_DGRAM) #create client socket
    message = 'ping' #message to be capitalized by server
    i = 0
    while i <= 10:
        start = datetime.now() #start time for rtt calc
        clientSocket.sendto(message,(serverName, serverPort)) #send to server
        clientSocket.settimeout(0.01) #timeout length
        try:
            newMess, serverAddress = clientSocket.recvfrom(2048)
            end = datetime.now() #end time for rtt calc
            rtt = (end - start)
            #printing of information
            print("{0}: Message:{1}\nRTT:{2}\n ".format(i, newMess, rtt))
        except timeout:
            #different printout if timeout occurs
            print("{0}: Timeout\n".format(i))
            start = 0
            rtt = 0
        i += 1 #iteration
        
    clientSocket.close() #close socket at end

    pass


if __name__ == '__main__':
    main()
    
