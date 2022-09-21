
import socket
sk=socket.socket()
addr=('192.168.0.110',9090)
sk.bind(addr)
sk.listen(3)

while True:
    conn,addr=sk.accept()
    print(addr)
    while True:
        try:
            data=conn.recv(1024)
        except Exception:
            break
        if not data:
            break
        print(str(data))
        inp=input('>>>>')
        conn.send(bytes(inp))