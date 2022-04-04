from app.main import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
import datetime


class AccessToken(db.Model):
    __tablename__ = "access_token"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    access_token = db.Column(db.String(100), nullable=False)
    refresh_id = db.Column(UUID(as_uuid=True), db.ForeignKey('refresh_token.id'),
                           nullable=False)
    expired_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())
    status = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())
    updated_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())
