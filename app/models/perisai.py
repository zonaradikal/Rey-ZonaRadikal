from app.extensions import db

class Perisai(db.Model):
    __tablename__ = "perisai"
    id = db.Column(db.Integer, primary_key=True)
    
    radioisotop = db.Column(db.String(20), nullable=False, index=True)
    material_perisai = db.Column(db.String(20), nullable=False, index=True)
    hvl = db.Column(db.Float, nullable=False)
    satuan_hvl = db.Column(db.String(30), nullable=False)
    __table_args__ = (
        db.UniqueConstraint(
            "radioisotop",
            "material_perisai",
            name="uq_perisai_radioisotop_material"
        ),
    )

    def __repr__(self):
        return f"<Perisai {self.radioisotop} - {self.material_perisai}>"