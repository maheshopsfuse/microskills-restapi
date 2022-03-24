from flask_restplus import Namespace, fields


class SignUpDto:
    api = Namespace('SignUp', description='User Registration')
    user = api.model('SignUp', {
        'email': fields.String(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'password': fields.String(required=True, description='user password'),
        'role': fields.String(required=True, description='user role')
    })
    rep_user = api.model("Response", {
        'success': fields.String(required=True, description='Status'),
        'id': fields.String(required=True, description='Id'),
        'authorization': fields.String(required=True, description='Authorization'),
        'email': fields.String(required=True, description='user email address'),
        'first_name': fields.String(required=True, description='user first name'),
        'last_name': fields.String(required=True, description='user last name'),
        'role': fields.String(required=True, description='user role')
    })
