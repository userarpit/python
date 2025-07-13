import socket

from _thread import start_new_thread
import threading

lock = threading.Lock()

def threaded(con):
    while True:
        data = con.recv(1024)

        if not data:
            print("Bye")
            lock.release()
            break

        data = data[::-1]

        con.send(data)

    con.close()

def main():
    host = ""
    port = 8080

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind to port = 8080
    s.bind((host,port))

    # listen
    s.listen(5)

    while True:

        con, adr = s.accept()

        # acquire lock
        lock.acquire()
        print(adr[0], adr[1])

        start_new_thread(threaded, (con,))

    s.close()

if __name__ == "__main__":
    main()