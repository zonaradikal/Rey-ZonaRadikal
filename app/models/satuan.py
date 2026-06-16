from app.extensions import db

class SatuanKonversi(db.Model):
    __tablename__ = "satuan_konversi"
    id = db.Column(db.Integer, primary_key=True)
    jenis_besaran = db.Column(db.String(50), nullable=False, index=True)
    
    satuan_asal = db.Column(db.String(30), nullable=False, index=True)
    satuan_tujuan = db.Column(db.String(30), nullable=False, index=True)
    faktor_konversi = db.Column(db.Float, nullable=False)
    __table_args__ = (
        db.UniqueConstraint(
            "jenis_besaran",
            "satuan_asal",
            "satuan_tujuan",
            name="uq_satuan_konversi"
        ),
    )

    def __repr__(self):
        return (
            f"<SatuanKonversi "
            f"{self.jenis_besaran}: "
            f"{self.satuan_asal} -> {self.satuan_tujuan}>"
        )