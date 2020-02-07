import socket

def main():
    host = socket.gethostbyname(input('enter host : '))

    port = 12345

    serversock =socket.socket()

    serversock.bind((host, port))

    serversock.listen(2)

    print("socket is listening for connections")

    while True:
        conn, addr = serversock.accept()

        print("connection initiated from " + str(addr))

        msg = "connection activated successfully"+ "\r\n"
        
        conn.send(msg.encode('ascii'))

        conn.close()


if __name__ == "__main__":
    main()
