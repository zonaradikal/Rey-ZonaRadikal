from app.extensions import db
from app.models.user import waktu_indonesia

class RiwayatAktivitas(db.Model):
    __tablename__ = "riwayat_aktivitas"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)

    radioisotop = db.Column(db.String(20), nullable=False, index=True)
    aktivitas_awal_input = db.Column(db.Float, nullable=False)
    satuan_awal = db.Column(db.String(20), nullable=False)

    aktivitas_awal = db.Column(db.Float, nullable=False)
    satuan_hasil = db.Column(db.String(20), nullable=False)

    tanggal_awal = db.Column(db.Date, nullable=False)
    tanggal_hitung = db.Column(db.Date, nullable=False)

    selang_hari = db.Column(db.Integer, nullable=False)
    waktu_paruh_hari = db.Column(db.Float, nullable=False)

    hasil_aktivitas = db.Column(db.Float, nullable=False)
    keterangan = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime(timezone=True), default=waktu_indonesia, nullable=False)
    user = db.relationship("User", back_populates="riwayat_aktivitas")

    def __repr__(self):
        return f"<RiwayatAktivitas {self.radioisotop} - User {self.user_id}>"