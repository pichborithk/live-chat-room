import random
from string import ascii_uppercase
from flask import request, jsonify, abort

from app import app
from app.models import Room, Response, UserRoom
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
def get_room(room_code):
    room = Room.get_room_by_code(room_code)
    print(room.messages)
    return jsonify({"message": "success"})
