import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientIP= socket.gethostbyname(socket.gethostname())
print clientIP
clientPort=111
client.connect((clientIP,clientPort))
ServerReply=client.recv(10)
print(ServerReply)
client.close()
