import random
from string import ascii_uppercase
from flask import request, jsonify, abort

from app import app
from app.models import Room, Response, UserRoom
from app.middleware.deserialize_auth import deserialize_auth


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
def create_room():
    payload = create_room.auth_payload
    room_code = generate_unique_code(4)
    new_room = Room(code=room_code)
    new_room.save()
    user_room_connect = UserRoom(user_id=payload["id"], room_id=new_room.id)
    user_room_connect.save()
    return jsonify({"message": "success"})
