from flask import Flask, request, escape

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "<div> <center> <h1> Cyber Heist </h1> </div> <div> <a href=\"/camera?cameraRotation=something&password=something\"> Camera View </a> </div> </center>"

HINTCOMMENT = "<!-- I really like udonnoodles :) -->"
@app.route("/camera", methods=["GET"])
def control():
    cameraRotation = request.args.get('cameraRotation')
    password = str(request.args.get('password'))
    
    if password == "udonnoodles":
        try:
            float(cameraRotation)
        except:
            return '<center> <h1> Invalid camera rotation </h1> </center>' + HINTCOMMENT

        if cameraRotation is not None:
            return '<center> <h1 style="color=green"> You solved it! Raise your hand and we will get you setup with the real thing :) </h1> <h1> Camera rotation set to: {} </h1> </center> {}'.format(escape(cameraRotation), HINTCOMMENT)
        else:
            return '<center> <h1> Camera rotation not set </h1> </center>' + HINTCOMMENT
    else:
        return '<center> <h1> Invalid password, the correct password must be provided to control the camera </h1> </center>' + HINTCOMMENT