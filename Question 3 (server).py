import random
import threading
import socket

quotes = ["'It always seems impossible until it is done.' \n Nelson Mandela",
        "'Try not to be a man of success, but a man of value.' \n Albert Einstein",
        "'All great achievements require time.' \n Maya Angelou",
        "'The world is full of magic things, patiently waiting for our senses to grow sharper.' \n W.B. Yeats"]
def function_quote(csocket):
    quote = random.choice(quotes)
    csocket.sendall(quote.encode())
    csocket.close()

def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("192.168.100.202", 8080))

    s.listen(5)
    print(" Listening on %s:%d for request" % ("192.168.100.202", 8080))

    while True:
        c, address = s.accept()
        print(" Accepted connection from %s" % str(address))
        cHandler = threading.Thread(target=function_quote, args=(c,))
        cHandler.start()

main()
