from app.main import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
import datetime


class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    course_name = db.Column(db.String, nullable=False)
    course_icon = db.Column(db.String, nullable=False)
    course_description = db.Column(db.String, nullable=False)
    course_duration = db.Column(db.String, nullable=False)

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'),
                        nullable=False)

    lesson = db.relationship('Lesson',
                             backref='courses')

    skill = db.relationship('Skill',
                            backref='courses')

    status = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())
    updated_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())
