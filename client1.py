import socket

host = '127.0.0.1'
port = 1030

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect it to server and port number
# host is the address of server
# port is the port of the server
s.connect((host, port))

# receive message string from server, at a time 1024 bytes
msg = s.recv(1024)

while msg:
    print('Received: ' + msg.decode())
    msg = s.recv(1024)


# closing the connection by closing the socket
s.close()