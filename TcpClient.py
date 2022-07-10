from socket import *
import time
import requests

serverName = 'localhost'
serverPort = 50007
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect( (serverName, serverPort) )

t1 = time.time()
# print ("connected to: " + str(serverName) + str(serverPort) )


# sentence = input('Please enter(hello):')
sentence = "hello"
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print( "Message received from Server: " + modifiedSentence.decode())

t2 = time.time()

print("RTT for TCP is", t2-t1)

clientSocket.close()



