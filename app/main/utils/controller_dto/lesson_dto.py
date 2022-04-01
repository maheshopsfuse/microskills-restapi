from flask_restplus import Namespace, fields


class LessonDto:
    api = Namespace('Lesson', description='Lesson')

    lesson = api.model('Lesson Details', {
        'lesson_id': fields.String(readOnly=True),
        'lesson_name': fields.String(required=True),
        'lesson_content': fields.String(required=True)
    })
    req_lessons = api.model("Lessons", {
        'lessons': fields.List(fields.Nested(lesson))
    })

    res_lessons = api.model("Lessons Response", {
        'success': fields.String(required=True, description='Status'),
        'course_id': fields.String(required=True),
        'lessons': fields.List(fields.Nested(lesson))
    })
