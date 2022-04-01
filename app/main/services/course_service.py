from app.main import db, save
from app.main.model.course import Course
from datetime import datetime

from app.main.services.signup_service import getUserId


def saveCourse(data, headers):
    user_id = getUserId(headers)
    if user_id:
        new_course = Course(
            course_name=data['course_name'], course_icon=data['course_icon'], course_description=data['course_description'], course_duration="4", user_id=user_id)
        save(new_course)
        response_object = {
            "success": True,
            "course_id": str(new_course.id),
            "course_name": new_course.course_name,
            "course_icon": new_course.course_icon,
            "course_description": new_course.course_description,
            "course_duration": new_course.course_duration,
            "user_id": str(new_course.user_id)
        }
        return response_object, 201
    response_object = {
        'success': False,
        'message': 'User Not Found',
    }
    return response_object, 409


def checkCourseId(id):
    course = db.session.query(Course).filter(Course.id == id).first()
    if course:
        return True
    return False


def getCourses(headers):
    user_id = getUserId(headers)
    if user_id:
        courses = db.session.query(Course).filter(
            Course.user_id == user_id).all()
        courses_list = []
        for i in courses:
            course = {"course_id": str(i.id), "course_name": i.course_name,
                      "course_description": i.course_description, 'course_icon': i.course_icon, 'course_duration': i.course_duration}
            courses_list.append(course)
        response_object = {
            'success': True,
            'user_id': user_id,
            'courses': courses_list
        }
        return response_object, 201
    response_object = {
        'success': False,
        'message': 'User Not Found',
    }
    return response_object, 409
