from flask_restplus import Api
from flask import Blueprint

from app.main.controller.signup_controller import api as signup_api
from app.main.controller.login_controller import api as login_api

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
    title='MicroSkills website backend',
    version='1.0',
    description='rest api in flask',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(signup_api, path='/')
api.add_namespace(login_api, path='/')
