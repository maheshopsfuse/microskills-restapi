from flask_restful import abort
from flask_restplus import Resource
from app.main.services.skill_service import getSkills, saveSkills
from app.main.utils.controller_dto.skill_dto import SkillDto
from app.main.utils.decorator_functions import admin_login_required
from flask import request, Response, jsonify

api = SkillDto.api

req_skills = SkillDto.req_skills
res_skills = SkillDto.res_skills

res_error = SkillDto.res_error


@api.route("api/course/<string:course_id>/skill")
class SkillController(Resource):
    @admin_login_required
    @api.expect(req_skills, validate=True)
    @api.response(201, "Success", res_skills)
    @api.response(401, "Failed", res_error)
    def post(self, course_id):
        data = request.json
        res, _ = saveSkills(data, course_id)
        if res['success'] == True:
            return res, 200
        return res, 401

    @ admin_login_required
    @api.response(201, "Success", res_skills)
    @api.response(401, "Failed", res_error)
    def get(self, course_id):
        res, _ = getSkills(course_id)
        if res['success'] == True:
            return res, 200
        return res, 401
