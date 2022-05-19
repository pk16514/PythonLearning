"""
\r\n signifies an EOL (end of line), so \r\n\r\n signifies nothing between two EOL sequences.
That is the equivalent of a blank line.
"""

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

# textfile retrieval

cmd1 = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd1)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end="")

mysock.close()
