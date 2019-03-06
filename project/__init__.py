from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import sys 

# instantiate app
app = Flask(__name__)

# set configuration
app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings) # new

# creae new sql database instance
db = SQLAlchemy(app) 

# first databse user model
class User(db.Model):  # new
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.String(128), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


@app.route("/user/ping", methods=["GET"])
def ping_pong():
    return jsonify({
        "status": "success",
        "message": "pong"
    })