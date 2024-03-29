from flask import Flask, request, escape
from servo import moveServo

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<div> <center> <h1> Cyber Heist </h1> </div> <div> <a href=\"/camera?cameraRotation=something&password=something\"> Camera View </a> </div> </center>"

@app.route("/camera", methods=["GET"])
def control():
    cameraRotation = request.args.get('cameraRotation')
    password = str(request.args.get('password'))

    if password == "udonnoodles":
        if cameraRotation is not None:
            moveServo(cameraRotation)
            return '<center> <h1> Camera rotation set to: {} </h1> <div><iframe scrolling="no" width=640px height=480px frameBorder="0" src="http://192.168.137.15:8000/index.html"></iframe><div> </center>'.format(escape(cameraRotation))
        else:
            return '<center> <h1> Camera rotation not set </h1> <div><iframe scrolling="no" width=640px height=480px frameBorder="0" src="http://192.168.137.15:8000/index.html"></iframe><div> </center>'
    else:
        return '<center> <h1> Invalid password, the correct password must be provided to control the camera </h1> </center>'