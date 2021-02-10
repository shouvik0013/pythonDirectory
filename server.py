import socket

host = '127.0.0.1'
port = 1030

# create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket with server address and port no.
s.bind((host, port))

# allow maximum 1 connection to the server
s.listen(1)

# wait until a client accepts the connection
# c is the connection object
# addr is the address of the client
c, addr = s.accept()
print('Address of the user is ' + str(addr))

# send a welcome message to the client
c.send(b'Hello user')
msg = 'bye'
c.send(msg.encode())

# disconnect the server by closing the connection object c
c.close()