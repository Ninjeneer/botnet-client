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
    pass
