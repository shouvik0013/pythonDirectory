import socket

host = '127.0.0.1'
port = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.connect((host, port))

# enter input

msg = str(input('Enter msg: '))

while msg != 'exit':
    s.send(msg.encode())

    # receive the response from the server
    data = s.recv(1024)
    print('Message from server: ' + str(data.decode()))


    # enter data
    msg = str(input('Enter msg: '))

# close the connection
s.close()
