from network import start_server
import asyncio

print('Starting botnet...')

print('Starting network handlers...')
asyncio.run(start_server())
print('Network handlers started.')

print('Botnet started')