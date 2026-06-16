from app.extensions import db

class Radioisotop(db.Model):
    __tablename__ = "radioisotop"
    id = db.Column(db.Integer, primary_key=True)
    
    radioisotop = db.Column(db.String(20), nullable=False, unique=True, index=True)
    waktu_paruh = db.Column(db.Float, nullable=False)
    satuan_waktu_paruh = db.Column(db.String(20), nullable=False)

    konstanta_gamma = db.Column(db.Float, nullable=False)
    satuan_konstanta_gamma = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Radioisotop {self.radioisotop}>"