from flask import request, jsonify, abort

from app import app
from app.models import Response, Message, Room
from app.middleware.auth import deserialize_auth, verification_user_in_room


@app.post("/api/<string:room_code>/messages")
@deserialize_auth
@verification_user_in_room
def new_message(current_user, room_code):
    room = Room.get_room_by_code(room_code)
    if not room:
        abort(403, f"Room with code {room_code} do not exist")

    # payload = new_message.auth_payload
    text = request.json.get("text")
    message = Message(text=text, sender_id=current_user["id"], room_id=room.id)
    message.save()
    # print(message.sender, message.text)
    # print(type(message.sender.user))
    response = Response(
        data={
            "id": message.id,
            "text": message.text,
            "sender": message.sender.username,
            "room": message.room.code,
        }
    )
    return jsonify(response.__dict__)


@app.get("/api/messages")
@deserialize_auth
def get_all_message():
    messages = Message.get_all()
    response = Response(data={"messages": messages})
    return jsonify(response.__dict__)
