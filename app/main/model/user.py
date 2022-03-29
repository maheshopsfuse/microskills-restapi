from app.main import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
import datetime

user_access_token = db.Table('user_access_token',
                             db.Column('user_id', UUID(as_uuid=True),
                                       db.ForeignKey('users.user_id')),
                             db.Column('access_id', UUID(as_uuid=True),
                                       db.ForeignKey('access_token.id'))
                             )


class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    role = db.Column(db.String(20), nullable=False)

    status = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())
    updated_at = db.Column(
        db.Numeric, default=datetime.datetime.utcnow().timestamp())

    access_token = db.relationship('AccessToken', secondary=user_access_token,
                                   backref='users')

    refresh_token = db.relationship('RefreshToken',
                                    backref='users', uselist=False)
