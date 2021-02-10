import socket

host = '127.0.0.1'
port = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind

s.bind((host, port))

s.listen(1)

c, addr = s.accept()
print('Client is connected...')
print('Address of the client: ' + str(addr))

while True:
    msg = c.recv(1024)

    if not msg:
        break
    print('From client: ' + str(msg.decode()))

    # enter response from server
    resp = str(input('Enter response: '))
    c.send(resp.encode())

c.close()