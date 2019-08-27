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
        return '<h1> Camera rotation set to: {} </h1> <div><iframe src="0.0.0.0:8000/index.html"></iframe><div>'.format(escape(cameraRotation))
    else:
        return '<h1> Camera rotation not set </h1> <div><iframe src="0.0.0.0:8000/index.html"></iframe><div>'