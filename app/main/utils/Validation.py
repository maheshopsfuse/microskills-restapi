from functools import wraps
from flask import request
from app.main.model.access_token import AccessToken
from app.main import db
from app.main.model.refresh_token import RefreshToken
from app.main.model.user import User
from datetime import datetime


def validate_access_token(token):
    access_token = token["Access"]
    _, user_id, _ = access_token.split('.')
    user = db.session.query(User).join(User.access_token).filter(User.user_id == user_id).filter(
        AccessToken.access_token == access_token
    ).filter(AccessToken.expired_at > datetime.utcnow().timestamp()).first()
    if user:
        return True
    return False


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
