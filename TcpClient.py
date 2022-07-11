from socket import *
import time
import requests
import datetime

serverName = 'localhost'
serverPort = 50007
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect( (serverName, serverPort) )
n = 10
while n>0:

    t1 = datetime.datetime.now()
    print("this is stage"+ str(n))
# print ("connected to: " + str(serverName) + str(serverPort) )


# sentence = input('Please enter(hello):')
    sentence = "hello"
    clientSocket.send(sentence.encode())
    print("at this process")

    #reciver form server
    modifiedSentence = clientSocket.recv(1024)
    print( "Message received from Server: " + modifiedSentence.decode())
    
    t2 = datetime.datetime.now()

    print("RTT for TCP is", t2-t1)
    n = n -1
# t2 = time.time()

# print("RTT for TCP is", t2-t1)

clientSocket.close()