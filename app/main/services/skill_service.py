from app.main import save, db
from app.main.model.lessons import Lesson
from app.main.model.skill import Skill
from app.main.services.course_service import checkCourseId


def saveSkills(data, id):
    course = checkCourseId(id)
    if course:
        skills = data['skills']
        skill_list = []
        for i in skills:
            skill = Skill(skill_name=i['skill_name'], course_id=id)

            save(skill)
            skill_list.append(
                {'skill_id': str(skill.id), 'skill_name': skill.skill_name})
        response_object = {
            'success': True,
            'course_id': id,
            'skills': skill_list
        }
        return response_object, 201
    response_object = {
        'success': False,
        'message': 'Course Not Found',
    }
    return response_object, 409


def getSkills(id):
    if checkCourseId(id):
        skills = db.session.query(Skill).filter(Skill.course_id == id).all()
        skill_list = []
        for i in skills:
            skill = {"skill_id": str(i.id), "skill_name": i.skill_name}
            skill_list.append(skill)
        response_object = {
            'success': True,
            'course_id': id,
            'skills': skill_list
        }
        return response_object, 201
    response_object = {
        'success': False,
        'message': 'Course Not Found',
    }
    return response_object, 409
