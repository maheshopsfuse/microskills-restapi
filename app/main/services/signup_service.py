from app.main.model.signup import SignUp
from app.main import db, save
from app.main.utils.PasswordEncryption import generateSalt, generatePassword
from app.main.utils.JWTToken import getToken, saveToken
from app.main.model.user_session import UserSession


def save_user(data):
    user = SignUp.query.filter_by(email=data['email']).first()
    if not user:
        salt = generateSalt()
        password = generatePassword(data['password'], salt)
        password = str(password) + ':' + str(salt)
        new_user = SignUp(
            email=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            password=password,
            role=data['role'],
        )
        save(new_user)
        token = saveToken(new_user.user_id)
        response_object = {
            "success": True,
            "id": new_user.user_id,
            "authorization": token,
            "email": new_user.email,
            "first_name": new_user.first_name,
            "last_name": new_user.last_name,
            "role": new_user.role
        }
        return response_object, 201
    else:
        response_object = {
            'success': False,
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409
