import string
import random

from app.main import save
from app.main.model.access_token import AccessToken
from app.main.model.refresh_token import RefreshToken


def randomString():
    length = 30
    ran = ''.join(random.choices(string.ascii_uppercase +
                                 string.digits + string.ascii_lowercase, k=length))
    return str(ran)


def getToken(user_id):
    return randomString() + '.' + user_id + '.' + randomString()


def saveToken(user_id):
    id = str(user_id)
    refresh = getToken(user_id=id)
    access = getToken(id)
    refreshToken = RefreshToken(refresh_token=refresh, user_id=user_id)
    save(refreshToken)
    accessToken = AccessToken(access_token=access, refresh_id=refreshToken.id)
    save(accessToken)
    return refreshToken, accessToken


def saveRefreshToken(user_id):
    id = str(user_id)
    token = getToken(id)
    refreshToken = RefreshToken(refresh_token=token, user_id=user_id)
    save(refreshToken)
    return token


def saveAccessToken(refresh):
    id = str(refresh.user_id)
    token = getToken(id)
    accessToken = AccessToken(access_token=token, refresh_id=refresh.id)
    save(accessToken)
    return token
