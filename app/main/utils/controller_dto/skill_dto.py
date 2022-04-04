from flask_restplus import Namespace, fields


class SkillDto:
    api = Namespace('Skill', description='Skill')

    skill = api.model('Skill Details', {
        'skill_id': fields.String(readOnly=True),
        'skill_name': fields.String(required=True)
    })
    req_skills = api.model("Skills", {
        'skills': fields.List(fields.Nested(skill))
    })
    res_skills = api.model("Skills Response", {
        'success': fields.String(required=True, description='Status'),
        'course_id': fields.String(required=True),
        'skills': fields.List(fields.Nested(skill))
    })
    res_error = api.model("Response Error", {
        'success': fields.String(required=True, description='success'),
        'message': fields.String(required=True, description='message')
    })
