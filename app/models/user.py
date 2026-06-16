from datetime import datetime
from zoneinfo import ZoneInfo

from app.extensions import db

def waktu_indonesia(): return datetime.now(ZoneInfo("Asia/Jakarta"))

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False, index=True)
    no_sertifikat_ppr = db.Column(db.String(100), nullable=True, index=True)

    password_hash = db.Column(db.String(255), nullable=False)

    role = db.Column(db.String(20), default="user", nullable=False)
    status = db.Column(db.String(20), default="pending", nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), default=waktu_indonesia, nullable=False)
    updated_at = db.Column(db.DateTime(timezone=True), default=waktu_indonesia, onupdate=waktu_indonesia, nullable=False)

    riwayat_aktivitas = db.relationship(
        "RiwayatAktivitas", back_populates="user", lazy=True, cascade="all, delete-orphan")
    riwayat_paparan = db.relationship(
        "RiwayatPaparan", back_populates="user", lazy=True, cascade="all, delete-orphan")
    riwayat_daerah_radiasi = db.relationship(
        "RiwayatDaerahRadiasi", back_populates="user", lazy=True, cascade="all, delete-orphan")
    sessions = db.relationship(
    "UserSession", back_populates="user", lazy=True, cascade="all, delete-orphan") 

    def __repr__(self):
        return f"<User {self.username}>"