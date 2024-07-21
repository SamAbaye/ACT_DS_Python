from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
print("Server Socket reated")

s.bind(('', 1234))
print("Address is binded")

s.listen(2)
print("Server is lstening")

conn, c_addr = s.accept()
print("Connection Accepted")

data = conn.recv(1024)
print("Message Receved from Client")
print(data.decode('utf-8'))

msg = input("Enter your Message")

conn.send(msg.encode('utf-8'))
print("Message Sent to Client!")

conn.close()
print("Connection Closed!")

s.close()
print("Socket Closed!")
