from flask import jsonify, session

from app.models import Panduan
from app.routes.main_bp import main_bp

# === KONSTANTA === #
KATEGORI_BANTUAN = {
    "beranda": "Umum",
    "riwayat": "Umum",
    "panduan": "Umum",
    "aktivitas": "Aktivitas",
    "paparan": "Paparan",
    "daerah": "Daerah",
}


# === ROUTE BANTUAN HALAMAN === #
@main_bp.route("/bantuan/<string:halaman>")
def bantuan_halaman(halaman):

    # === CEK LOGIN === #
    if not session.get("user_id"):
        return jsonify({
            "error": "Pengguna belum login."
        }), 401

    # === AMBIL KATEGORI === #
    kategori = KATEGORI_BANTUAN.get(halaman.lower())
    if not kategori:
        return jsonify([])

    # === AMBIL DATA PANDUAN === #
    daftar_panduan = (
        Panduan.query
        .filter_by(
            kategori=kategori,
            is_active=True
        )
        .order_by(Panduan.urutan.asc())
        .all()
    )

    # === FORMAT RESPONSE === #
    data = [
        {
            "kategori": item.kategori,
            "judul": item.judul,
            "isi": item.isi,
            "urutan": item.urutan,
        }
        for item in daftar_panduan
    ]

    # === RETURN JSON === #
    return jsonify(data)