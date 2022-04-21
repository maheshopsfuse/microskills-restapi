from flask import request
from flask_restplus import Resource
from app.main.services.role_service import saveRole
from app.main.utils.controller_dto.error_dto import res_error
from app.main.utils.controller_dto.role_dto import RoleDto

api = RoleDto.api
req_role = RoleDto.req_role
res_role = RoleDto.res_role


@api.route("api/role")
class RoleController(Resource):
    @api.expect(req_role, validate=True)
    @api.response(201, "Success", res_role)
    @api.response(401, "Failed", res_error)
    def post(self):
        data = request.json
        res, _ = saveRole(data)
        if res['success'] == True:
            return res, 200
        return res, 401
