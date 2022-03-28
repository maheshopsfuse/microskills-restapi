from flask import request
from flask_restplus import Resource
from app.main.services.access_token_service import generateAccessToken
from app.main.utils.controller_dto.access_token_dto import AccessTokenDto
from app.main.utils.controller_dto.error_dto import rep_error

api = AccessTokenDto.api
req_token = AccessTokenDto.token
rep_token = AccessTokenDto.rep_token


@api.route("api/access-token")
class AccessTokenController(Resource):
    @api.expect(req_token, validate=True)
    def post(self):
        data = request.json
        rep, _ = generateAccessToken(data)
        if rep['success'] == True:
            return api.marshal(rep, rep_token)
        return api.marshal(rep, rep_error)
