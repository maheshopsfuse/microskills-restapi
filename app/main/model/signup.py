from app.main import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from app.main.model.user_session import UserSession


class SignUp(db.Model):
    __tablename__ = "users"
    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String(20), nullable=False)
    user_session = db.relationship('UserSession',
                                   backref='users')
