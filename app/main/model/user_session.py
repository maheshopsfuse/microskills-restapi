from app.main import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class UserSession(db.Model):
    __tablename__ = "user_session"
    session_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    session_token = db.Column(db.String(100), nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'),
                        nullable=False)
