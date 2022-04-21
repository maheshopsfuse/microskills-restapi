from app.main import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
import datetime


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    role_name = db.Column(db.String(20), nullable=False)
    role_desc = db.Column(db.String(50), nullable=False)

    status = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())
    updated_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())

    user_role = db.relationship('UserRole',
                                backref='roles', uselist=False)
