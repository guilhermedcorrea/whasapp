from app import app, socketio

if __name__ == '__main__':
    # Use this for development mode
    #socketio.run(app, host='192.168.1.105', port='5000')
    socketio.run(app, host='172.17.0.186', port='5000')

    # Use this for production
    #socketio.run(app)

