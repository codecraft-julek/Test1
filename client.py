import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

nickname = input("Choose your nickname: ")

def receive():
    while True:
        try: 
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                pass
            else:
                print(message)
        except:
            print("An error occurred!")
           
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'

        receive_thread = threading.Thread(target=receive)
        receive_thread.start()

        write_thread = threading.Thread(target=write)
        write_thread.start()