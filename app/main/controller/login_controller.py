from flask import request
from flask_restplus import Resource
from app.main.services.login_service import login
from app.main.utils.validation import authenticate
from app.main.utils.controller_dto.error_dto import rep_error
from app.main.utils.controller_dto.login_dto import LoginDto

api = LoginDto.api
_login = LoginDto.req_login
rep_login = LoginDto.rep_login


@api.route("api/login")
class LoginController(Resource):
    @api.expect(_login, validate=True)
    @authenticate
    def post(self):
        data = request.json
        rep, _ = login(data)
        if rep['success'] == True:
            return api.marshal(rep, rep_login)
        return api.marshal(rep, rep_error)
