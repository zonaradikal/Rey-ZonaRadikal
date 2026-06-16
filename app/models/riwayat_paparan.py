from app.extensions import db
from app.models.user import waktu_indonesia

class RiwayatPaparan(db.Model):
    __tablename__ = "riwayat_paparan"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)

    kondisi_perisai = db.Column(db.String(30), nullable=False)
    radioisotop = db.Column(db.String(20), nullable=False, index=True)

    konstanta_gamma = db.Column(db.Float, nullable=False)
    satuan_konstanta_gamma = db.Column(db.String(50), nullable=False)

    aktivitas_input = db.Column(db.Float, nullable=False)
    satuan_aktivitas = db.Column(db.String(20), nullable=False)
    aktivitas = db.Column(db.Float, nullable=False)

    jarak_input = db.Column(db.Float, nullable=False)
    satuan_jarak = db.Column(db.String(20), nullable=False)
    jarak = db.Column(db.Float, nullable=False)

    material_perisai = db.Column(db.String(20), nullable=True)
    tebal_perisai_input = db.Column(db.Float, nullable=True)
    satuan_tebal_perisai = db.Column(db.String(20), nullable=True)
    tebal_perisai = db.Column(db.Float, nullable=True)

    hvl = db.Column(db.Float, nullable=True)
    satuan_hvl = db.Column(db.String(20), nullable=True)

    laju_paparan = db.Column(db.Float, nullable=False)
    satuan_laju_paparan = db.Column(db.String(50), nullable=False)
    keterangan = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime(timezone=True), default=waktu_indonesia, nullable=False)
    user = db.relationship("User", back_populates="riwayat_paparan")

    def __repr__(self):
        return f"<RiwayatPaparan {self.radioisotop} - User {self.user_id}>"