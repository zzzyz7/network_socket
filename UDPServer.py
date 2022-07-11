import sys
# print (sys.version)
from socket import *
serverHost = ''
serverPort = 50007
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(( serverHost, serverPort))
# serverSocket.listen(1)


print ( 'The server is ready to receive ' )
n = 10
while n>0:
# connectionID, addr = serverSocket.accept()
# print ("The server connected to: " + str(addr) )
# sentence = serverSocket.recv(1024).decode()
        bytesAddressPair = serverSocket.recvfrom(1024)

        data = bytesAddressPair[0].decode()

        address = bytesAddressPair[1]

# sentence = serverSocket.recv(1024).decode()
        clientMsg = "Message received from Client:" + data

# print ("Message received from client: " + str(data))
        print(clientMsg)
        # capitalizedSentence = sentence.upper()
        # # print ("upcased: " + str(capitalizedSentence ))
        # # connectionID.send(capitalizedSentence.encode())

        reply = "back at you"
        bytesToSend  = str.encode(reply)

        serverSocket.sendto(bytesToSend,address)
        n = n -1


serverSocket.close()