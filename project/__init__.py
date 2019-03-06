from flask import Flask, jsonify
import os
import sys 

# instantiate app
app = Flask(__name__)

# set configuration
app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings) # new


@app.route("/user/ping", methods=["GET"])
def ping_pong():
    return jsonify({
        "status": "success",
        "message": "pong"
    })