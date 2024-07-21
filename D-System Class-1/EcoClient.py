from socket import socket, AF_INET, SOCK_STREAM

eC = socket(AF_INET, SOCK_STREAM)

eC.connect(('localhost', 1234))


while(True):
    eC.send("Hi".encode("utf-8"))

    data = eC.recv(1024)
    print("Message Recieved")
    print(data.decode("utf-8"))
    eC.conn.close()
eC.close()
print("Socket Closed!")
