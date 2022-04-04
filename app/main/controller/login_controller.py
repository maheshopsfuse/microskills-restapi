from flask import request
from flask_restplus import Resource
from app.main.services.login_service import login
from app.main.utils.controller_dto.error_dto import res_error
from app.main.utils.controller_dto.login_dto import LoginDto

api = LoginDto.api
_login = LoginDto.req_login
res_login = LoginDto.res_login


@api.route("api/login")
class LoginController(Resource):
    @api.expect(_login, validate=True)
    @api.response(201, "Success", res_login)
    @api.response(401, "Failed", res_error)
    def post(self):
        data = request.json
        res, _ = login(data)
        if res['success'] == True:
            return res, 200
        return res, 401
