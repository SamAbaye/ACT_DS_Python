from socket import socket, AF_INET, SOCK_STREAM

c = socket(AF_INET, SOCK_STREAM)
print("Client Connection Created")

c.connect(('localhost', 1234))
print("Connection eastablshed wth Server")

msg = input("Enter Your Message")

c.send(msg.encode("utf-8"))
print("Message Sent")

data = c.recv(1024)
print("Message Recieved")
print(data.decode("utf-8"))

c.close()
print("Socket Closed!")
