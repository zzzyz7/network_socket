import sys
# print (sys.version)
from socket import *
serverHost = ''
serverPort = 50007
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(( serverHost, serverPort))
# serverSocket.listen(1)


print ( 'The server is ready to receive ' )
# while True:
# connectionID, addr = serverSocket.accept()
# print ("The server connected to: " + str(addr) )
sentence = serverSocket.recv(1024).decode()
print ("Message received from client: " + str(sentence ))
        # capitalizedSentence = sentence.upper()
        # # print ("upcased: " + str(capitalizedSentence ))
        # # connectionID.send(capitalizedSentence.encode())

reply = "back at you"

serverSocket.sendto(reply.encode(),("localhost",serverPort))



# serverSocket.close()