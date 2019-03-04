from flask import Flask, jsonify

# instantiate app
app = Flask(__name__)

# set configuration
app.config.from_object("project.config.DevelopmentConfig") # new

@app.route("/user/ping", methods=["GET"])
def ping_pong():
    return jsonify({
        "status": "success",
        "message": "pong"
    })