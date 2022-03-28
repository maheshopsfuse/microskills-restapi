from app.main.model.refresh_token import RefreshToken
from app.main.utils.jwt_token import saveAccessToken


def generateAccessToken(data):

    token = RefreshToken.query.filter_by(
        refresh_token=data['refresh_token']).first()
    if token:
        new_token = saveAccessToken(token)
        response_object = {
            'success': True,
            "access_token": str(new_token)
        }
        return response_object, 201
