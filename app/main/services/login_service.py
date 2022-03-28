from app.main import save, db
from app.main.model.login import Login
from app.main.model.user import User
from app.main.utils.jwt_token import saveToken
from app.main.utils.password_encryption import validatePassword


def login(data):
    user = User.query.filter_by(email=data['email']).first()
    if user:
        password, salt = user.password.split(':')
        passwordValidation = validatePassword(
            data['password'], password, salt)
        if passwordValidation:
            logged_user = Login(email=data['email'], password=data['password'])
            save(logged_user)
            refresh, access = saveToken(user.user_id)
            user.access_token.append(access)
            db.session.commit()
            response_object = {
                'success': True,
                "id": user.user_id,
                "refresh_token": refresh.refresh_token,
                "access_token": access.access_token,
                "email": user.email
            }
            return response_object, 201
        else:
            response_object = {
                'success': False,
                'message': 'Invalid username or Password.'
            }
            return response_object, 401
    else:
        response_object = {
            'success': False,
            'message': 'User not exists. Please SignUp in.',
        }
        return response_object, 409
