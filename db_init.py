from app import create_app
from app.extensions import db

from app.models import (
    User,
    Isotop,
    Perisai,
    SatuanKonversi,
    Panduan,
    FAQ,
    RiwayatAktivitas,
    RiwayatPaparan,
    RiwayatDaerahRadiasi,
)

from app.utils.seed_database import seed_database


app = create_app()

with app.app_context():
    db.create_all()
    seed_database()
    print("Database, tabel, dan data awal berhasil dibuat.")