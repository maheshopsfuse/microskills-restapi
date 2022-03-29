from app.main.model.refresh_token import RefreshToken
from app.main.utils.jwt_token import saveAccessToken
from app.main import db
from datetime import datetime


def generateAccessToken(data):
    token = db.session.query(RefreshToken).filter(
        RefreshToken.refresh_token == data['refresh_token']
    ).filter(RefreshToken.expired_at > datetime.utcnow().timestamp()).first()
    if token:
        new_token = saveAccessToken(token)
        response_object = {
            'success': True,
            "access_token": str(new_token)
        }
        return response_object, 201
    return {'success': False, 'message': "Invalid Token"}, 401
