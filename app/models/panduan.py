from app.extensions import db

class Panduan(db.Model):
    __tablename__ = "panduan"

    id = db.Column(db.Integer, primary_key=True)

    kategori = db.Column(db.String(50), nullable=False, index=True)
    judul = db.Column(db.String(150), nullable=False)
    
    isi = db.Column(db.Text, nullable=False)
    urutan = db.Column(db.Integer, nullable=False, default=1)

    is_active = db.Column(db.Boolean, default=True, nullable=False)

    __table_args__ = (
        db.UniqueConstraint(
            "kategori",
            "judul",
            name="uq_panduan_kategori_judul"
        ),
    )

    def __repr__(self):
        return f"<Panduan {self.kategori} - {self.judul}>"