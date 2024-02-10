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
    sio.emit('drive', data)


@sio.event
def steer(sid, data):
    sio.emit('steer', data)


@sio.event
def Escape(sid):
    sys.exit()


if __name__ == '__main__':
    your_ip_address = '0.0.0.0'
    your_port = 5001

    # Use eventlet to run the server with WebSocket support
    eventlet.wsgi.server(eventlet.listen((your_ip_address, your_port)), app)
