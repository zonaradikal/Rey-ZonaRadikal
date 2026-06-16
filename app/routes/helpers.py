from flask import session, request
from app.models.user import waktu_indonesia

from app.extensions import db
from app.models import (User, UserSession, RiwayatAktivitas, RiwayatPaparan, RiwayatDaerahRadiasi,)


# === USER === #
def get_current_user():
    user_id = session.get("user_id")
    if not user_id:
        return None
    return db.session.get(User, user_id)


# === FORMAT TANGGAL === #
def format_tanggal(nilai_tanggal):
    if not nilai_tanggal:
        return ""
    return nilai_tanggal.strftime("%Y-%m-%d")


# === FORMAT RIWAYAT AKTIVITAS === #
def format_riwayat_aktivitas(item):
    return {
        "id": item.id,
        "jenis_perhitungan": "aktivitas",
        "judul_hasil": item.keterangan or "Perhitungan Aktivitas Sumber",
        "created_at": item.created_at,
        "input_data": {
            "radioisotop": item.radioisotop,
            "aktivitas_awal": item.aktivitas_awal_input,
            "satuan_awal": item.satuan_awal,
            "tanggal_awal": format_tanggal(item.tanggal_awal),
            "tanggal_hitung": format_tanggal(item.tanggal_hitung),
            "keterangan": item.keterangan,
        },
        "hasil_data": {
            "hasil_aktivitas": item.hasil_aktivitas,
            "satuan_hasil": item.satuan_hasil,
        },
    }


# === FORMAT RIWAYAT PAPARAN === #
def format_riwayat_paparan(item):
    return {
        "id": item.id,
        "jenis_perhitungan": "paparan",
        "judul_hasil": item.keterangan or "Perhitungan Laju Paparan",
        "created_at": item.created_at,
        "input_data": {
            "kondisi_perisai": item.kondisi_perisai,
            "radioisotop": item.radioisotop,
            "aktivitas": item.aktivitas_input,
            "satuan_aktivitas": item.satuan_aktivitas,
            "jarak": item.jarak_input,
            "satuan_jarak": item.satuan_jarak,
            "material_perisai": item.material_perisai,
            "tebal_perisai": item.tebal_perisai_input,
            "satuan_tebal_perisai": item.satuan_tebal_perisai,
            "keterangan": item.keterangan,
        },
        "hasil_data": {
            "laju_paparan": item.laju_paparan,
            "satuan_laju_paparan": item.satuan_laju_paparan,
        },
    }


# === FORMAT RIWAYAT DAERAH === #
def format_riwayat_daerah(item):
    return {
        "id": item.id,
        "jenis_perhitungan": "daerah",
        "judul_hasil": item.keterangan or "Perhitungan Daerah Radiasi",
        "created_at": item.created_at,
        "input_data": {
            "pembatas_dosis": item.pembatas_dosis,
            "jam_kerja": item.jam_kerja,
            "laju_paparan": item.laju_paparan,
            "satuan_paparan": item.satuan_paparan,
            "jarak_acuan": item.jarak_acuan,
            "faktor_okupansi": item.faktor_okupansi,
            "keterangan": item.keterangan,
        },
        "hasil_data": {
            "hasil_pengendalian": item.hasil_pengendalian,
            "hasil_supervisi": item.hasil_supervisi,
        },
    }


# === RIWAYAT === #
def get_all_riwayat(user_id):
    riwayat_aktivitas = RiwayatAktivitas.query.filter_by(user_id=user_id).all()
    riwayat_paparan = RiwayatPaparan.query.filter_by(user_id=user_id).all()
    riwayat_daerah = RiwayatDaerahRadiasi.query.filter_by(user_id=user_id).all()

    data_riwayat = []
    data_riwayat.extend(format_riwayat_aktivitas(item) for item in riwayat_aktivitas)
    data_riwayat.extend(format_riwayat_paparan(item) for item in riwayat_paparan)
    data_riwayat.extend(format_riwayat_daerah(item) for item in riwayat_daerah)

    data_riwayat.sort(key=lambda item: item["created_at"], reverse=True)
    return data_riwayat


# === SIDEBAR RIWAYAT === #
def get_sidebar_riwayat(user_id, limit=5):
    return get_all_riwayat(user_id)[:limit]

# === UPDATE SESSION === #
def update_session_activity():

    session_log_id = session.get("session_log_id")
    if not session_log_id:
        return


    session_log = db.session.get(
        UserSession,
        session_log_id
    )
    if not session_log:
        return

    session_log.last_activity_at = waktu_indonesia()

    db.session.commit()