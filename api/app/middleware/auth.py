from functools import wraps
import jwt
from flask import request, abort

from app import app
from app.models import User


def deserialize_auth(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        auth = request.headers.get("Authorization")
        prefix = auth[:7]
        if not auth or prefix != "Bearer ":
            abort(401, "Invalid Token")

        token = auth[7:]
        try:
            payload = jwt.decode(
                jwt=token, key=app.config["SECRET_KEY"], algorithms=["HS256"]
            )
        except (jwt.ExpiredSignatureError, jwt.InvalidSignatureError) as error:
            # print(error.args)
            # print(f"{error=}")
            abort(401, f"{error}")
        # setattr(decorated_function, "auth_payload", payload)
        return func(current_user=payload, *args, **kwargs)

    return decorated_function


def verification_user_in_room(func):
    @wraps(func)
    def decorated_function(current_user, room_code, *args, **kwargs):
        user = User.get_user_by_id(current_user["id"])
        rooms = user.get_all_room_code()
        if room_code not in rooms:
            abort(401, "Unauthorized")

        print("User may enter this room")

        return func(room_code, *args, **kwargs)

    return decorated_function
