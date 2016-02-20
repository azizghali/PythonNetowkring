import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverIP= socket.gethostbyname(socket.gethostname())
print serverIP
serverPort=111
server.bind((serverIP,serverPort))
server.listen(2)
(client, ip)=server.accept()
client.send("How are you network engineers")
client.close()