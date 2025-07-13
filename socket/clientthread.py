import socket


def main():
    host="127.0.0.1"
    port = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host,port))
    str1 = "hello"
    while True:
        s.send(str1.encode('ascii'))
        reverse_str1 = s.recv(1024)
        print(str(reverse_str1.decode('ascii')))

        ans = input("Want to send more data (Y/N)")
        if ans == 'N':
            break
        
    s.close()

if __name__ == "__main__":
    main()