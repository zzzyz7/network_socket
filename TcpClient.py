from socket import *
import time
import requests

serverName = 'localhost'
serverPort = 50007
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect( (serverName, serverPort) )


# print ("connected to: " + str(serverName) + str(serverPort) )


sentence = input('Please enter(hello):')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print( "Message received from Server: " + modifiedSentence.decode())

clientSocket.close()



def RTT(url):
 
    # time when the signal is sent
    t1 = time.time()
 
    r = requests.get(url)
 
    # time when acknowledgement of signal
    # is received
    t2 = time.time()
 
    # total time taken
    tim = str(t2-t1)
 
    print("Time in seconds :" + tim)

url= 'http://localhost'

RTT(url)