from app.main import save, db
from app.main.model.lessons import Lesson
from app.main.services.course_service import checkCourseId


def saveLessons(data, id):

    course = checkCourseId(id)
    if course:
        lessons = data['lessons']
        lesson_list = []
        for i in lessons:
            lesson = Lesson(lesson_name=i['lesson_name'],
                            lesson_content=i['lesson_content'], course_id=id)
            save(lesson)
            lesson_list.append({'lesson_id': str(lesson.id), 'lesson_name': lesson.lesson_name,
                                'lesson_content': lesson.lesson_content})
        response_object = {
            'success': True,
            'course_id': id,
            'lessons': lesson_list
        }
        return response_object, 201
    response_object = {
        'success': False,
        'message': 'Course Not Found',
    }
    return response_object, 409


def getLessons(id):
    if checkCourseId(id):
        lessons = db.session.query(Lesson).filter(Lesson.course_id == id).all()
        lessons_list = []
        for i in lessons:
            lesson = {"lesson_id": str(i.id), "lesson_name": i.lesson_name,
                      "lesson_content": i.lesson_content}
            lessons_list.append(lesson)
        response_object = {
            'success': True,
            'course_id': id,
            'lessons': lessons_list
        }
        return response_object, 201
    response_object = {
        'success': False,
        'message': 'Course Not Found',
    }
    return response_object, 409
