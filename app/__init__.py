from flask_restplus import Api
from flask import Blueprint

from app.main.controller.registration_controller import api as reg_ns
from app.main.controller.skill_controller import api as skill_ns
from app.main.controller.signup_controller import api as signup_ns
from app.main.controller.login_controller import api as login_ns

blueprint = Blueprint('api', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(
    blueprint,
    title='Micro Skill website backend',
    version='1.0',
    description='rest api in flask',
    authorizations=authorizations,
    security='apikey'
)


api.add_namespace(reg_ns, path='/')
api.add_namespace(skill_ns, path='/')
api.add_namespace(signup_ns, path='/')
api.add_namespace(login_ns, path='/')
