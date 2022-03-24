from flask_restplus import Model, Namespace, fields


class LoginDto:
    api = Namespace('Login', description='User Login')
    req_login = api.model("Request Login", {
        'email': fields.String(required=True, description='email address'),
        'password': fields.String(required=True, description='Password')
    })
    rep_login = api.model("Response Model", {
        'success': fields.String(required=True, description=' Status'),
        'id': fields.String(required=True, description='Id'),
        'email': fields.String(required=True, description='email address'),
        'authorization': fields.String(required=True, description='Authorization')
    })
