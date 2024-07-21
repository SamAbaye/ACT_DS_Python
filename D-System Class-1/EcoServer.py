from socket import socket, AF_INET, SOCK_STREAM

eS = socket(AF_INET, SOCK_STREAM)

eS.bind(('', 1234))

eS.listen(3)

conn, c_addr = eS.accept()
while(True):
    data = conn.recv(1024)
    print(data.decode("utf-8"))

    conn.send(data)

conn.close()
