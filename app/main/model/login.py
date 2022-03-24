from app.main import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class Login(db.Model):
    __tablename__ = "login"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(20), nullable=False)
