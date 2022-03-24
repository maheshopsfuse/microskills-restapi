import string
import random
from app.main import save

from app.main.model.user_session import UserSession


def randomString():
    length = 30
    ran = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits + string.ascii_lowercase, k=length))
    return str(ran)


def getToken(user_id):
    return randomString() + '.' + user_id + '.' + randomString()


def saveToken(user_id):
    id = str(user_id)
    jwt_token = getToken(user_id=id)
    session = UserSession(
        session_token=jwt_token, user_id=id)
    save(session)
    return jwt_token
