from app.main.model.role import Role
from app.main.model.user import User
from app.main import db, save
from app.main.model.user_role import UserRole
from app.main.utils.password_encryption import generateSalt, generatePassword
from app.main.utils.jwt_token import saveToken


def save_user(data):
    user = User.query.filter_by(email=data['email']).first()
    role = checkRole(data['role'])
    if not user and role:
        salt = generateSalt()
        password = generatePassword(data['password'], salt)
        password = str(password) + ':' + str(salt)
        new_user = User(
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            password=password,
        )
        save(new_user)
        user_role = UserRole(user_id=new_user.user_id, role_id=role.id)
        save(user_role)
        refresh, access = saveToken(new_user.user_id)
        new_user.access_token.append(access)
        db.session.commit()
        response_object = {
            "success": True,
            "id": str(new_user.user_id),
            "refresh_token": refresh.refresh_token,
            "access_token": access.access_token,
            "email": new_user.email,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "role": role.role_name
        }
        return response_object, 201
    else:
        response_object = {
            'success': False,
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409


def getUserId(data):
    access_token = data["Access"]
    _, user_id, _ = access_token.split('.')
    user = db.session.query(User).filter(
        User.user_id == user_id)
    if user:
        return user_id
    return None


def checkRole(role):
    role = db.session.query(Role).filter(Role.role_name == role).first()
    return role
