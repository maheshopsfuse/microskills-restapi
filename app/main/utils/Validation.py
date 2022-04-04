
from app.main.model.access_token import AccessToken
from app.main import db
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


def validate_user_admin(token):
    validate_token = validate_access_token(token)
    if validate_token:
        access_token = token["Access"]
        _, user_id, _ = access_token.split('.')
        user = db.session.query(User).filter(
            User.user_id == user_id).filter(User.role == 'admin')
        if user:
            return True
    return False
