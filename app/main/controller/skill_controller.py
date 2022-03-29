from flask_restplus import Resource
from app.main.utils.validation import authenticate
from app.main.utils.controller_dto.skill_dto import SkillDto
from flask import Response
api = SkillDto.api


@api.route("api/add-skill")
class SkillController(Resource):
    @authenticate
    def post(self):
        return {'success': True}, 201
