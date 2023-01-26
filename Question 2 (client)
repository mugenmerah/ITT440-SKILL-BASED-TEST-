import socket

def main():
    #Create socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Connection to server and port.
    s.connect(("192.168.100.202", 8080))

    #Input temperature in fahrenheit to be convert
    temp_far = input("Enter temperature in Fahrenheit: ")
    s.send(temp_far.encode())
    #Receive message from server and output
    temp_cel = s.recv(1024).decode()
    print("Temperature [Celsius] :",temp_cel)


main()
