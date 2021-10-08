# Botnet client

**For education purpose only.**

# Installation

Requirements:
- Python >= 3

Optional:
- Docker

## Running without Docker

Install python required modules
```bash
python -m pip install -r requirements.txt
```

Set required environment variables:
- CENTRAL_SERVER_IP
- CENTRAL_SERVER_PORT

Run the app
```bash
python app.py
```


## Running with Docker

Run the container
```bash
docker run -e CENTRAL_SERVER_IP=XXXXXXX -e CENTRAL_SERVER_PORT=XXXXXXX ninjeneer/dev:botnet-client -d
```

*For localhost usage, use **host.docker.internal** as CENTRAL_SERVER_IP*