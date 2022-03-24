from flask import request
from flask_restplus import Resource
from app.main.services.signup_service import save_user
from app.main.utils.controller_dto.signup_dto import SignUpDto
from app.main.utils.controller_dto.error_dto import rep_error

api = SignUpDto.api
_user = SignUpDto.user
rep_user = SignUpDto.rep_user


@api.route("api/signup")
class Registration(Resource):
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        rep, _ = save_user(data)
        if rep['success'] == True:
            return api.marshal(rep, rep_user)
        return api.marshal(rep, rep_error)
