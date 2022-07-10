from socket import *
import time


serverName = 'localhost'
serverPort = 50007
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect( (serverName, serverPort) )

t1 = time.time()
# print ("connected to: " + str(serverName) + str(serverPort) )


# sentence = input('Please enter(hello):')
sentence = "hello"
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print( "Message received from Server: " + modifiedSentence.decode())

# t2 = time.time()
# print(t2)

# print("RTT for UDP is", t2-t1)



clientSocket.close()

t2 = time.time()


print("RTT for UDP is", t2-t1)


