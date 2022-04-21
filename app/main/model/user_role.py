from app.main import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
import datetime


class UserRole(db.Model):
    __tablename__ = "user_role"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'),
                        nullable=False)
    role_id = db.Column(UUID(as_uuid=True), db.ForeignKey('roles.id'),
                        nullable=False)

    status = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())
    updated_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())
