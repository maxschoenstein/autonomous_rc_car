FROM arm32v7/python:3.7-slim-buster

WORKDIR /usr/src/app

COPY ./src/templates ./templates
COPY ./src/hmi.py ./hmi.py
COPY ./requirements.txt ./requirements.txt

ARG pyenv=/usr/local/bin/python3

RUN apt-get update
RUN apt-get install -y build-essential

RUN ${pyenv} -m pip install --upgrade pip 
RUN ${pyenv} -m pip install picamera

# RUN pip install -r requirements.txt

CMD ["python", "./hmi.py"]
