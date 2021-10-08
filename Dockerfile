FROM python:3.9-alpine

ADD . /app/
WORKDIR /app

RUN python3 -m pip install -r requirements.txt
CMD python3 app.py