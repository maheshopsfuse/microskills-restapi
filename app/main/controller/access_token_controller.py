from flask import request
from flask_restplus import Resource
from app.main.services.access_token_service import generateAccessToken
from app.main.utils.controller_dto.access_token_dto import AccessTokenDto
from app.main.utils.controller_dto.error_dto import res_error

api = AccessTokenDto.api
req_token = AccessTokenDto.token
res_token = AccessTokenDto.res_token


@api.route("api/access-token")
class AccessTokenController(Resource):
    @api.expect(req_token, validate=True)
    @api.response(201, "Success", res_token)
    @api.response(401, "Failed", res_error)
    def post(self):
        data = request.json
        res, _ = generateAccessToken(data)
        if res['success'] == True:
            return res, 200
        return res, 401
