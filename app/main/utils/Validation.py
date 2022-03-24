from functools import wraps
from flask import request, Response


def validate_token(token):
    print(token)
    return "hello"


def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.headers
        validate_token(auth)
        return f(*args, **kwargs)
    return wrapper
