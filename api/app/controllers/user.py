from datetime import datetime, timedelta
import bcrypt
import jwt
from flask import request, jsonify, abort

from app import app
from app.models import User, Response
from app.middleware.auth import deserialize_auth


@app.post("/api/users/register")
def register():
    # body = request.get_json()
    username = request.json.get("username")
    user_ = User.get_user_by_username(username)
    if user_:
        abort(403, f"User with name {username} already exist")

    password = request.json.get("password")
    byte_password = bytes(password, "utf-8")
    hashed_password = bcrypt.hashpw(password=byte_password, salt=bcrypt.gensalt(8))
    new_user = User(username=username, password=hashed_password)
    new_user.save()

    expiration = datetime.utcnow() + timedelta(days=1)
    payload = {
        "id": new_user.id,
        "username": username,
        "exp": expiration,
    }
    token = jwt.encode(
        payload=payload,
        key=app.config["SECRET_KEY"],
        algorithm="HS256",
    )

    response = Response(
        data={
            "message": "Success create new account",
            "token": token,
        }
    )
    return jsonify(response.__dict__)


@app.post("/api/users/login")
def login():
    username = request.json.get("username")
    user = User.get_user_by_username(username)
    if not user:
        abort(403, f"User with name {username} do not exist")

    password = request.json.get("password")
    byte_password = bytes(str(password), "utf-8")
    if not bcrypt.checkpw(byte_password, user.password):
        abort(403, "Unauthorized")

    expiration = datetime.utcnow() + timedelta(days=1)
    payload = {
        "id": user.id,
        "username": username,
        "exp": expiration,
    }
    token = jwt.encode(
        payload=payload,
        key=app.config["SECRET_KEY"],
        algorithm="HS256",
    )

    response = Response(
        data={
            "message": "Success create new account",
            "token": token,
        }
    )
    return jsonify(response.__dict__)


@app.get("/api/users/me")
@deserialize_auth
def get_user(current_user):
    # payload = get_user.auth_payload
    user = User.get_user_by_id(current_user["id"])
    # messages = [message.text for message in user.messages]
    response = Response(
        data={
            "id": user.id,
            "username": user.username,
            "rooms": user.get_all_room_code(),
        }
    )
    return jsonify(response.__dict__)
