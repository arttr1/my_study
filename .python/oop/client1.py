import socket
import threading

class Client:
    def __init__(self, host='localhost', port=11111):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.bind((host, 11112))
        self.client.connect((host,port))
        print('Connection succesful')
    
    def get_message(self):
        while True:
            try:
                message = self.client.recv(1024).decode()
                print(f'Получено:', message)
            except:
                print('Connect close')
                self.client.close()
                break
    
    def send(self):
        while True:
            message = input()
            self.client.send(message.encode())

    def run(self):
        receive_thread = threading.Thread(target=self.get_message)
        receive_thread.start()
        send_thread = threading.Thread(target=self.send)
        send_thread.start()

if __name__ == '__main__':
    client = Client()
    client.run()