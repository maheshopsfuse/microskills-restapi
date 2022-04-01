from flask import request
from flask_restplus import Resource
from app.main.services.signup_service import save_user
from app.main.utils.controller_dto.signup_dto import SignUpDto
from app.main.utils.controller_dto.error_dto import res_error

api = SignUpDto.api
_user = SignUpDto.user
res_user = SignUpDto.res_user


@api.route("api/signup")
class Registration(Resource):
    @api.expect(_user, validate=True)
    @api.response(201, "Success", res_user)
    @api.response(401, "Failed", res_error)
    def post(self):
        data = request.json
        res, _ = save_user(data)
        if res['success'] == True:
            return res, 200
        return res, 401
