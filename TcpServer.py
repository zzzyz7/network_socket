import sys
# print (sys.version)
from socket import *
serverHost = ''
serverPort = 50007
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(( serverHost, serverPort))
serverSocket.listen(1)
print ( 'The server is ready to receive ' )
connectionID, addr = serverSocket.accept()

n = 10
while n>0:
        
# print ("The server connected to: " + str(addr) )
        sentence = connectionID.recv(1024).decode()
        print("got the passage")
        print ("Message received from client: " + str(sentence ))
        # capitalizedSentence = sentence.upper()
        # # print ("upcased: " + str(capitalizedSentence ))
        # # connectionID.send(capitalizedSentence.encode())

        reply = "back at you"

        connectionID.send(reply.encode())
        n = n -1



serverSocket.close()