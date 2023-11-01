import random
from string import ascii_uppercase
from flask import request, jsonify, abort

from app import app
from app.models import Room, Response, UserRoom, User
from app.middleware.auth import deserialize_auth, verification_user_in_room


def generate_unique_code(length):
    rooms = Room.get_all_code()
    while True:
        code = ""
        for _ in range(length):
            code += random.choice(ascii_uppercase)

        if code not in rooms:
            break

    return code


@app.post("/api/rooms/create")
@deserialize_auth
def create_room(current_user):
    # payload = create_room.auth_payload
    room_code = generate_unique_code(4)
    new_room = Room(code=room_code)
    new_room.save()
    user_room_connect = UserRoom(user_id=current_user["id"], room_id=new_room.id)
    user_room_connect.save()
    response = Response(data={"code": room_code})
    return jsonify(response.__dict__)


@app.get("/api/rooms/<string:room_code>")
@deserialize_auth
@verification_user_in_room
def get_room(current_user, room_code):
    room = Room.get_room_by_code(room_code)
    if not room:
        abort(403, f"Room with code {room_code} do not exist")

    messages = room.get_all_messages()
    response = Response(data=messages)
    return jsonify(response.__dict__)


@app.post("/api/rooms/join/<string:room_code>")
@deserialize_auth
def join_room(current_user, room_code):
    room = Room.get_room_by_code(room_code)
    if not room:
        abort(403, f"Room with code {room_code} do not exist")

    user = User.get_user_by_id(current_user["id"])
    rooms = user.get_all_room_code()
    if room_code not in rooms:
        user_room_connect = UserRoom(user_id=current_user["id"], room_id=room.id)
        user_room_connect.save()

    messages = room.get_all_messages()
    response = Response(data=messages)
    return jsonify(response.__dict__)
