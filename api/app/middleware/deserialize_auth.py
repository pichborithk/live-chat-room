from functools import wraps
import jwt
from flask import request, abort

from app import app


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
        setattr(decorated_function, "auth_payload", payload)
        return func(*args, **kwargs)

    return decorated_function
