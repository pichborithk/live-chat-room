import jwt
from flask import request, jsonify, abort

from app import app
from app.models import Response, Message
from app.middleware.deserialize_auth import deserialize_auth


@app.post("/api/messages")
@deserialize_auth
def new_message():
    payload = new_message.auth_payload
    text = request.json.get("text")
    message = Message(text=text, sender_id=payload["id"])
    message.save()
    # print(message.sender, message.text)
    # print(type(message.sender.user))
    response = Response(
        data={"message": message.text, "sender": message.sender.username}
    )
    return jsonify(response.__dict__)