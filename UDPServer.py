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
# sentence = serverSocket.recv(1024).decode()
bytesAddressPair = serverSocket.recvfrom(1024)

data = bytesAddressPair[0]

address = bytesAddressPair[1]

# sentence = serverSocket.recv(1024).decode()
clientMsg = "Message received from Client:{}".format(data)

# print ("Message received from client: " + str(data))
print(clientMsg)
        # capitalizedSentence = sentence.upper()
        # # print ("upcased: " + str(capitalizedSentence ))
        # # connectionID.send(capitalizedSentence.encode())

reply = "back at you"
bytesToSend  = str.encode(reply)

<<<<<<< HEAD
serverSocket.sendto(reply.encode(),("localhost",serverPort))

=======
serverSocket.sendto(bytesToSend,address)
>>>>>>> 14cd4fe2e49a2a50a22afee39466d62248e8e7d4


serverSocket.close()