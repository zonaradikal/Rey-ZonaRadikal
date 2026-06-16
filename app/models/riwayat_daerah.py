from app.extensions import db
from app.models.user import waktu_indonesia

class RiwayatDaerahRadiasi(db.Model):
    __tablename__ = "riwayat_daerah_radiasi"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)

    pembatas_dosis = db.Column(db.Float, nullable=False)
    jam_kerja = db.Column(db.Float, nullable=False)
    laju_paparan = db.Column(db.Float, nullable=False)
    satuan_paparan = db.Column(db.String(20), nullable=False)
    laju_paparan_msv = db.Column(db.Float, nullable=False)

    jarak_acuan = db.Column(db.Float, nullable=False)
    satuan_jarak_acuan = db.Column(db.String(10), nullable=False, default="m")
    faktor_okupansi = db.Column(db.Float, nullable=False)

    batas_pengendalian_tahun = db.Column(db.Float, nullable=False)
    batas_supervisi_tahun = db.Column(db.Float, nullable=False)
    batas_pengendalian_jam = db.Column(db.Float, nullable=False)
    batas_supervisi_jam = db.Column(db.Float, nullable=False)

    hasil_pengendalian = db.Column(db.Float, nullable=False)
    hasil_supervisi = db.Column(db.Float, nullable=False)
    estimasi_dosis_tahun = db.Column(db.Float, nullable=False)

    keterangan = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime(timezone=True), default=waktu_indonesia, nullable=False)
    user = db.relationship("User", back_populates="riwayat_daerah_radiasi")

    def __repr__(self):
        return f"<RiwayatDaerahRadiasi User {self.user_id}>"