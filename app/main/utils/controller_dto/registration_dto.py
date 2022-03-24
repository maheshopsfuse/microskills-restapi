from flask_restplus import Namespace, fields


class RegistrationDto:
    api = Namespace('Regitration', description='User Registration')
    req_reg_user = api.model("request Register", {
        'email': fields.String(required=True, description='email address')
    })
