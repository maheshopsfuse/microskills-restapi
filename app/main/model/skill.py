from app.main import db
from sqlalchemy.dialects.postgresql import UUID
import datetime


class Skill(db.Model):
    __tablename__ = "skill"
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    category_name = db.Column(db.String(20), nullable=False)
    category_icon = db.Column(db.String(20), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

    status = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self,  category_name, category_icon, skill_name):
        self.category_name = category_name
        self.category_icon = category_icon
        self.skill_name = skill_name
