from socket import *

serverName = "10.173.204.63"
serverPort = 12345
clientSocket = socket(AF_INET, SOCK_DGRAM)
print("Connected with server on [", gethostbyname(gethostname()), "]")

while True:
    message = input('Input your expression:')
    clientSocket.sendto(message.encode() , (serverName, serverPort))

    if(message.replace(' ','') == "0/0="):
        clientSocket.close()
        print("User input ends; end the client program")
        break
    else:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print("Answer from server:", modifiedMessage.decode())