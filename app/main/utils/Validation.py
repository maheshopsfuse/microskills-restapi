from functools import wraps
from flask import request


def validate_token(token):
    token["Access"]
    user_id = ""
    return "hello"


def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.headers
        validate_token(auth)
        return f(*args, **kwargs)
    return wrapper
