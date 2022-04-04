from uuid import uuid4
from app.main import db
from sqlalchemy.dialects.postgresql import UUID
import datetime


class Skill(db.Model):
    __tablename__ = "skills"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    skill_name = db.Column(db.String(20), nullable=False)

    course_id = db.Column(UUID(as_uuid=True), db.ForeignKey('courses.id'),
                          nullable=False)

    status = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())
    updated_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())
