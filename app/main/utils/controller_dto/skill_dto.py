from flask_restplus import Namespace, fields


class SkillDto:
    api = Namespace('Skill', description='Add Skill')
    req_reg_skill = api.model("request Skill", {
        'email': fields.String(required=True, description='email address')
    })
