from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<h1> Cyber Heist </h1>"

@app.route("/camera", methods=["GET"])
def control():
    cameraRotation = request.args.get('cameraRotation')
    password = str(request.args.get('password'))

    if password == "udonnoodles":
        if cameraRotation is not None:
            return '<center> <h1> Camera rotation set to: {} </h1> </center>'.format(escape(cameraRotation))
        else:
            return '<center> <h1> Camera rotation not set </h1> </center>'
    else:
        return '<center> <h1> Invalid password, the correct password must be provided to control the camera </h1> </center>'