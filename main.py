import socket 

msgFromClient       = ":)"
bytesToSend = str. codificação (msgFromClient)

servidorAddressPort = ("127.0.0.1", 20001)
bufferSize          = 1024

# Criado socket UDP Client.

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Enviado para o Servidor usado o socket UDP Client.

UDPClientSocket.sendto(bytesToSend, serverAddressPort)
msgFromServer = UDPClientSocket. recvfrom (bufferSize)

msg = "Mensagem do Servidor:{}".format(msgFromServer[0])
print(msg)
