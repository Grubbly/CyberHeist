from flask import Flask, request, escape
from servo import moveServo

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<h1> Cyber Heist </h1>"

@app.route("/camera", methods=["GET"])
def control():
    cameraRotation = request.args.get('cameraRotation')

    if cameraRotation is not None:
        moveServo(cameraRotation)
        return '<h1> Camera rotation set to: {} </h1>'.format(escape(cameraRotation))
    else:
        return 'Camera rotation not set'