import socket
import time

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

cmd2 = b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n'
mysock.sendall(cmd2)

picture = b""
count = 0
while True:
    data_ = mysock.recv(5120)
    if len(data_) < 1:
        break
    time.sleep(0.25)
    count += len(data_)
    print(len(data_), count)
    picture += data_

mysock.close()

pos = picture.find(b"\r\n\r\n")
print('Header length', pos)
print(picture[:pos + 2].decode())

picture = picture[pos + 4:]
print(type(picture))
fhand = open("stuff.jpg", "wb")
fhand.write(picture)
fhand.close()
