from app.extensions import db

class FAQ(db.Model):
    __tablename__ = "faq"

    id = db.Column(db.Integer, primary_key=True)

    kategori = db.Column(db.String(100), nullable=False, index=True)
    pertanyaan = db.Column(db.String(255), nullable=False)
    jawaban = db.Column(db.Text, nullable=False)

    dasar_hukum = db.Column(db.Text, nullable=True)
    urutan = db.Column(db.Integer, nullable=False, default=1)
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    __table_args__ = (
        db.UniqueConstraint(
            "kategori",
            "pertanyaan",
            name="uq_faq_kategori_pertanyaan"
        ),
    )

    def __repr__(self):
        return f"<FAQ {self.kategori} - {self.pertanyaan}>"