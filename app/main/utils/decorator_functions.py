from functools import wraps
from flask import request
from app.main.utils.validation import validate_user_role

from app.main.utils.validation import validate_access_token, validate_user_admin


def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.headers
        token = validate_access_token(auth)
        if not token:
            response_object = {
                'success': False,
                'message': 'Invalid Token.'
            }
            return response_object
        return f(*args, **kwargs)
    return wrapper


def admin_login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.headers
        token = validate_user_admin(auth)
        if not token:
            response_object = {
                'success': False,
                'message': 'Invalid Token.'
            }
            return response_object
        return f(*args, **kwargs)
    return wrapper


def validate_role(role):
    def inner_decorator(f):
        def wrapped(*args, **kwargs):
            auth = request.headers
            if not validate_user_role(auth, role):
                response_object = {
                    'success': False,
                    'message': 'Invalid Role.'
                }
                return response_object
            return f(*args, **kwargs)
        return wrapped
    return inner_decorator
