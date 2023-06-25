from socket import *

serverPort = 12345
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('127.0.0.1', serverPort))
print("Connected by client on [", serverSocket.getsockname()[0], "]")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode()

    if(modifiedMessage.replace(' ','') == "0/0="):
        print("Received question '0 / 0 ='; end the server program")
        break
    else:
        ans = str(eval(modifiedMessage.replace('=','')))
        print(f"Received question '{modifiedMessage}' ; send back answer {ans}")
        serverSocket.sendto(ans.encode(), clientAddress)
    
