import sys

import socketio
import eventlet
import eventlet.wsgi

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print(f"Client connected: {sid}")


@sio.event
def disconnect(sid):
    print(f"Client disconnected: {sid}")


@sio.event
def drive(sid, data):
    print(f'drive: {data}')
    # sio.emit('drive', data)


@sio.event
def steer(sid, data):
    print(f'steer: {data}')
    # sio.emit('steer', data)


@sio.event
def steerSensitivity(sid, data):
    print(f'steerSensitivity: {data}')
    # sio.emit('steerSensitivity', data)


@sio.event
def driveSensitivity(sid, data):
    print(f'driveSensitivity: {data}')
    # sio.emit('driveSensitivity', data)


@sio.event
def power(sid, data):
    print(f'power: {data}')
    # sio.emit('power', data)


@sio.event
def exit(sid, data):
    print(f'exit: {data}')
    # sio.emit('exit', True)


@sio.event
def neutral(sid, data):
    print(f'neutral: {data}')
    # sio.emit('neutral', True)


@sio.event
def Escape(sid):
    sys.exit()


if __name__ == '__main__':
    your_ip_address = 'localhost'
    your_port = 5001

    # Use eventlet to run the server with WebSocket support
    eventlet.wsgi.server(eventlet.listen((your_ip_address, your_port)), app)
