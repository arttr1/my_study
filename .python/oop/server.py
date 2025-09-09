import socket
import threading

class Server:
    def __init__(self, host='localhost', port=11111):
        self.clients = {}  # сокет -> адрес
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(2)
        print(f'Server running on {host}:{port}')

    def message_send(self, message, client):
        for user in self.clients:
            if user != client:
                try:
                    user.send(message.encode())
                except:
                    del self.clients[user]

    def message_processing(self, user):
        while True:
            try:
                message = user.recv(1024).decode()
                if message:
                    client_addr = self.clients[user]
                    print(f'Get a message from {client_addr}: {message}')
                    self.message_send(message, user)
                else:
                    raise Exception('User off')
            except:
                print(f'Client {self.clients.get(user, "unknown")} disconnected.')
                if user in self.clients:
                    del self.clients[user]
                user.close()
                break

    def run(self):
        while True:
            user, addr = self.server.accept()
            print(f'Client on: {addr}')
            self.clients[user] = addr
            threading.Thread(target=self.message_processing, args=(user,)).start()

if __name__ == '__main__':
    server = Server()
    server.run()
