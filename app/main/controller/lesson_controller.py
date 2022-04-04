from flask_restplus import Resource
from app.main.services.lesson_service import getLessons,  saveLessons
from app.main.utils.controller_dto.lesson_dto import LessonDto
from app.main.utils.decorator_functions import admin_login_required
from flask import request
from app.main.utils.controller_dto.error_dto import res_error

api = LessonDto.api

req_lessons = LessonDto.req_lessons
res_lessons = LessonDto.res_lessons


@api.route("api/course/<string:course_id>/lesson")
class LessonController(Resource):
    @admin_login_required
    @api.expect(req_lessons, validate=True)
    @api.response(201, "Success", res_lessons)
    @api.response(401, "Failed", res_error)
    def post(self, course_id):
        data = request.json
        res, _ = saveLessons(data, course_id)
        if res['success'] == True:
            return res, 200
        return res, 401

    @admin_login_required
    @api.response(201, "Success", res_lessons)
    @api.response(401, "Failed", res_error)
    def get(self, course_id):
        res, _ = getLessons(course_id)
        if res['success'] == True:
            return res, 200
        return res, 401
