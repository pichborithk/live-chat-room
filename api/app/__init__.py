import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.ext.declarative import declarative_base
from flask_migrate import Migrate
from flask_socketio import SocketIO, send, emit
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.config["SECRET_KEY"] = bytes(os.getenv("APP_SECRET_KEY"), "utf-8")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_PATH")
CORS(app)
db = SQLAlchemy(app)
Base = declarative_base()
migrate = Migrate(app, db)
socketio = SocketIO(app, cors_allowed_origins="http://localhost:5173")


@app.get("/ping")
def ping():
    return jsonify({"success": True, "data": {"message": "pong"}, "error": False})


@socketio.on("message")
def message(data):
    content = {
        "id": data["id"],
        "text": data["text"],
        "sender": data["sender"],
    }
    emit("message", content, broadcast=True)
    # rooms[room_code]["messages"].append(content)
    print(f"{data['sender']} said: {data['text']}")


from app.controllers import *
