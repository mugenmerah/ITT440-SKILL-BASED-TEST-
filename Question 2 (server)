import socket
#Convert fahrenheit to celsius
def fahrenheit_to_celsius(temp_far):
    temp_cel = (temp_far - 32) * (5/9)
    return temp_cel

def main():
    #Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Bind the socket to host and port
    s.bind(("192.168.100.202", 8080))
    print(f"Server socket binding....")

    #Listening for connection
    s.listen(1)
    print(f"Server socket listening ...")


    while True:

        client_sock, addr = s.accept()
        print("[CONNECTION] From %s" % str(addr))

        temp_far = client_sock.recv(1024).decode()
        temp_cel = fahrenheit_to_celsius(float(temp_far))
        temp_cel = round(temp_cel,2)
        temp_cel = str(temp_cel)
        client_sock.send(temp_cel.encode())

main()
