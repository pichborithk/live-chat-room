from datetime import datetime, timedelta
import bcrypt
import jwt
from flask import request, jsonify, abort
from app import app, db
from .models import User


class Response:
    def __init__(
        self,
        data,
        error=False,
        success=True,
    ):
        self.success = success
        self.error = error
        self.data = data


@app.get("/ping")
def ping():
    return jsonify({"success": True, "data": {"message": "pong"}, "error": False})


@app.post("/api/users/register")
def register():
    # body = request.get_json()
    username = request.json.get("username")
    user_ = db.session.query(User).filter_by(username=username).first()
    if user_:
        abort(403, f"User with name {username} already exist")

    password = request.json.get("password")
    byte_password = bytes(password, "utf-8")
    hashed_password = bcrypt.hashpw(password=byte_password, salt=bcrypt.gensalt(8))
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    expiration = datetime.utcnow() + timedelta(seconds=120)
    payload = {"username": username, "exp": expiration}
    token = jwt.encode(payload=payload, key=app.config["SECRET_KEY"], algorithm="HS256")
    response = Response(error=False, data={"message": "Success create new account", "token": token})
    return jsonify(response.__dict__)


@app.post("/api/users/login")
def login():
    ...


# Error Handler
@app.errorhandler(404)
def handler_404(err):
    error = {"name": err.name, "message": err.description}
    return jsonify({"success": False, "error": error}), 404


@app.errorhandler(403)
def handler_403(err):
    error = {"name": err.name, "message": err.description}
    return jsonify({"success": False, "error": error}), 403
