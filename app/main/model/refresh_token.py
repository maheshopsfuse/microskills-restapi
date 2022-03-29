import datetime
from app.main import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class RefreshToken(db.Model):
    __tablename__ = "refresh_token"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    refresh_token = db.Column(db.String(100), nullable=False)
    expired_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey('users.user_id'))

    access_token = db.relationship('AccessToken',
                                   backref='refresh_token')
