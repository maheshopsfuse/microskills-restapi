from flask_restplus import Model, Namespace, fields


class LoginDto:
    api = Namespace('Login', description='User Login')
    req_login = api.model("Request Login", {
        'email': fields.String(required=True, description='email address'),
        'password': fields.String(required=True, description='Password')
    })
    res_login = api.model("Response Model", {
        'success': fields.String(required=True, description=' Status'),
        'id': fields.String(required=True, description='Id'),
        'email': fields.String(required=True, description='email address'),
        'access_token': fields.String(required=True, description='Access Token'),
        'refresh_token': fields.String(required=True, description='Refresh Token')
    })
