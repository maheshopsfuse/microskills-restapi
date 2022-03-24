from flask_restplus import Resource
from flask import request
from app.main.model.skill import Skill
from app.main.utils.controller_dto.skill_dto import SkillDto
from twilio.rest import Client
from datetime import datetime

api = SkillDto.api


@api.route("api/add-skill")
class SkillController(Resource):
    def post(self):
        print("hello")
