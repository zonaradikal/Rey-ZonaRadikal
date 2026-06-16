from datetime import datetime
from zoneinfo import ZoneInfo
from app.extensions import db

def waktu_indonesia(): return datetime.now(ZoneInfo("Asia/Jakarta"))

class UserSession(db.Model):
    __tablename__ = "user_sessions"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    login_at = db.Column(db.DateTime(timezone=True), default=waktu_indonesia, nullable=False)
    logout_at = db.Column(db.DateTime(timezone=True), nullable=True)

    last_activity_at = db.Column(db.DateTime(timezone=True), default=waktu_indonesia, nullable=False)
    
    ip_address = db.Column(db.String(50), nullable=True)
    user_agent = db.Column(db.Text, nullable=True)

    is_online = db.Column(db.Boolean, default=True, nullable=False)
    user = db.relationship("User", back_populates="sessions")

    def __repr__(self):
        return f"<UserSession {self.user_id}>"