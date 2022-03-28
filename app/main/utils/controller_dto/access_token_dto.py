from flask_restplus import Namespace, fields


class AccessTokenDto:
    api = Namespace('AccessToken', description='Token')
    token = api.model('AccessToken', {
        'refresh_token': fields.String(required=True, description='Access Token'),
    })
    rep_token = api.model("Response", {
        'success': fields.String(required=True, description='Status'),
        'access_token': fields.String(required=True, description='Authorization'),
    })
