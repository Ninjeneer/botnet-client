from typing import List
from flask import Flask
import requests
import json

app = Flask(__name__)
botnet_ip: str = ""
known_botnets: List[str] = []

def start_server():
    app.run()

def identify_to_central_server() -> bool:
    """
    Identify the botnet to the central server.
    Receives a JSON response { ip: the_botnet_ip, botnets: [ known_ip_list ] }
    """
    global known_botnets
    global botnet_ip

    response = requests.post("http://central_server_url")
    if response.status_code == 200:
        # Successfully identified, save already known botnets
        data = json.loads(response.text)
        botnet_ip = data['ip']
        known_botnets = data['botnets']
        return True
    
    return False

def identify_to_other_botnets() -> bool:
    """
    Connect to other botnets
    Remove from known_botnets unreachable IPs
    """
    global known_botnets
    global botnet_ip

    for ip in known_botnets:
        # Do not connect to itself
        if botnet_ip != ip:
            response = requests.post(botnet_ip + "/connect")
            if response.status_code != 200:
                # If IP is unreachable, remove it from known botnets
                known_botnets = filter(lambda x: x != ip, known_botnets)

# Http route definitions
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'