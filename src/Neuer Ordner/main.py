
import logging
import sys

from flask import Flask, render_template
from flask_socketio import SocketIO

from pwm_control import PWMControl
from drive_control import DriveControl

IP_ADDRESS = '192.168.0.170'
PORT = 5000

app = Flask(__name__)
socketio = SocketIO(app)
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('forward')
def forward():
    drive_control.increase_duty_cycle()

@socketio.on('backward')
def backward():
    drive_control.decrease_duty_cycle()

@socketio.on('right')
def right():
    steer_control.increase_duty_cycle()

@socketio.on('left')
def left():
    steer_control.decrease_duty_cycle()

@socketio.on('exit')
def exit():
    steer_control.exit()
    drive_control.exit()
    sys.exit()

if __name__ == '__main__':
    #steer_control = PWMControl(18, 50, 9.5, 4, 6.5, 0.25)
    drive_control = DriveControl(19, 270, 60, 20, 35, 1)
    socketio.run(app, host=IP_ADDRESS, port=PORT, debug=True)

