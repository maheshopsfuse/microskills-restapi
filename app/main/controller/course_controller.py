from flask_restplus import Resource
from app.main.services.course_service import getCourses, saveCourse
from app.main.utils.controller_dto.course_dto import CourseDto
from app.main.utils.decorator_functions import admin_login_required
from flask import request
from app.main.utils.controller_dto.error_dto import res_error

api = CourseDto.api
req_course = CourseDto.req_course
res_course = CourseDto.res_course

res_courses = CourseDto.res_courses


@api.route("api/course")
class CourseController(Resource):
    @admin_login_required
    @api.expect(req_course, validate=True)
    @api.response(201, "Success", res_course)
    @api.response(401, "Failed", res_error)
    def post(self):
        data = request.json
        res, _ = saveCourse(data, request.headers)
        if res['success'] == True:
            return res, 200
        return res, 401

    @admin_login_required
    @api.response(201, "Success", res_courses)
    @api.response(401, "Failed", res_error)
    def get(self):
        headers = request.headers
        res, _ = getCourses(headers)
        if res['success'] == True:
            return res, 200
        return res, 401
