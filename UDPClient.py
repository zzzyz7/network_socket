from socket import *
import datetime


serverName = 'localhost'
serverPort = 50007
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect( (serverName, serverPort) )


# print ("connected to: " + str(serverName) + str(serverPort) )
n = 10
while n>0:
# sentence = input('Please enter(hello):')
    t1 = datetime.datetime.now()
    sentence = "hello"
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print( "Message received from Server: " + modifiedSentence.decode())
    
    t2 = datetime.datetime.now()
    result = t2 - t1
    
    print("RTT for UDP is", result)
    n = n - 1
 

# t2 = time.time()
# print(t2)

# print("RTT for UDP is", t2-t1)




clientSocket.close()
