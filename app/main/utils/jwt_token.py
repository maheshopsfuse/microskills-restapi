import string
import random
import calendar
import time

from app.main import save
from app.main.model.access_token import AccessToken
from app.main.model.refresh_token import RefreshToken
from datetime import datetime, timedelta
from app.main.config import DevelopmentConfig


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
    refreshToken = RefreshToken(
        refresh_token=refresh, user_id=user_id, expired_at=getRefreshTokenTimeStamp())
    save(refreshToken)
    accessToken = AccessToken(
        access_token=access, refresh_id=refreshToken.id, expired_at=getAccessTokenTimeStamp())
    save(accessToken)
    return refreshToken, accessToken


def saveRefreshToken(user_id):
    id = str(user_id)
    token = getToken(id)
    refreshToken = RefreshToken(
        refresh_token=token, user_id=user_id, expired_at=getRefreshTokenTimeStamp())
    save(refreshToken)
    return token


def saveAccessToken(refresh):
    id = str(refresh.user_id)
    token = getToken(id)

    accessToken = AccessToken(
        access_token=token, refresh_id=refresh.id, expired_at=getAccessTokenTimeStamp())
    save(accessToken)
    return token


def getAccessTokenTimeStamp():
    date = datetime.utcnow() + timedelta(DevelopmentConfig.ACCESS_TOKEN_EXPIRE_IN_DAYS)
    return date.timestamp()


def getRefreshTokenTimeStamp():
    date = datetime.utcnow() + timedelta(DevelopmentConfig.REFRESH_TOKEN_EXPIRE_IN_DAYS)
    return date.timestamp()
