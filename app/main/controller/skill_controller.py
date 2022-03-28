from flask_restplus import Resource
from app.main.utils.controller_dto.skill_dto import SkillDto

api = SkillDto.api


@api.route("api/add-skill")
class SkillController(Resource):
    def post(self):
        print("hello")
