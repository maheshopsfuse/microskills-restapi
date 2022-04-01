from app.main import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
import datetime


class Lesson(db.Model):
    __tablename__ = "lessons"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    lesson_name = db.Column(db.String, nullable=False)
    lesson_content = db.Column(db.String, nullable=False)

    course_id = db.Column(UUID(as_uuid=True), db.ForeignKey('courses.id'),
                          nullable=False)

    status = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())
    updated_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())
