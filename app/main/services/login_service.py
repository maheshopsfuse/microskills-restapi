from app.main import save
from app.main.model.login import Login
from app.main.model.signup import SignUp
from app.main.utils.JWTToken import saveToken
from app.main.utils.PasswordEncryption import validatePassword


def login(data):
    user = SignUp.query.filter_by(email=data['email']).first()
    if user:
        password, salt = user.password.split(':')
        passwordValidation = validatePassword(
            data['password'], password, salt)
        if passwordValidation:
            logged_user = Login(email=data['email'], password=data['password'])
            save(logged_user)
            token = saveToken(user.user_id)
            response_object = {
                'success': True,
                "id": user.user_id,
                "authorization": token,
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
