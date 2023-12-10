import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000')
# sio.wait()

while True:
    msg = input("Enter a Number to send (or 'exit' to quit): ")
    if msg == 'exit':
        print('Disconnecting')
        break
    else:
        try:
            number = int(msg)
            sio.emit('my_message', number)
        except ValueError as e:
            print('Only numbers are allowed! Try again.')
