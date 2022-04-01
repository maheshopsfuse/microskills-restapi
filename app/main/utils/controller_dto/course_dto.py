from flask_restplus import Namespace, fields
from app.main.utils.controller_dto.lesson_dto import LessonDto
from app.main.utils.controller_dto.skill_dto import SkillDto


class CourseDto:
    api = Namespace('Course', description='Course')
    req_course = api.model('Course Details', {
        'course_id': fields.String(readOnly=True),
        'course_name': fields.String(required=True, description='Course Name'),
        'course_description': fields.String(required=True),
        'course_icon': fields.String(required=True),
        'course_duration': fields.String(required=True)
    })
    res_course = api.model("Course Response", {
        'success': fields.String(required=True, description='Status'),
        'user_id': fields.String(required=True),
        'course_id': fields.String(required=True),
        'course_name': fields.String(required=True, description='Course Name'),
        'course_description': fields.String(required=True),
        'course_icon': fields.String(required=True),
        'course_duration': fields.String(required=True)
    })
    res_courses = api.model("List Course Response", {
        'success': fields.String(required=True, description='Status'),
        'user_id': fields.String(required=True),
        'courses': fields.List(fields.Nested(req_course))
    })
