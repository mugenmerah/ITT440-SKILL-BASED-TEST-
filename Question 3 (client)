import socket

def main():

    csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    csocket.connect(("192.168.100.202", 8080))

    quote = csocket.recv(1024)
    print("Hi ! Here is your Quotes Of The Day! : \n %s" % quote.decode())

    csocket.close()

main()
