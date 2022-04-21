
from app.main.model.access_token import AccessToken
from app.main import db
from app.main.model.role import Role
from app.main.model.user import User
from datetime import datetime

from app.main.model.user_role import UserRole


def validate_access_token(headers):
    access_token = headers["Access"]
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


def validate_user_role(headers, role):
    token = validate_access_token(headers)
    if token:
        access_token = headers["Access"]
        _, user_id, _ = access_token.split('.')

        if isinstance(role, str):
            user_role = db.session.query(UserRole).join(Role).filter(
                UserRole.user_id == user_id).filter(Role.role_name == role).first()
        else:
            user_role = db.session.query(UserRole).join(Role).filter(
                UserRole.user_id == user_id).filter(Role.role_name.in_(role)).first()
        if user_role:
            return True
    return False
    #ret = db.session.query(Role).filter(Role.role_name == role)
