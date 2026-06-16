from datetime import datetime
from flask import render_template, redirect, url_for, session, request, flash

from app.extensions import db
from app.models import RiwayatAktivitas
from app.models.user import waktu_indonesia
from app.routes.main_bp import main_bp
from app.routes.helpers import get_current_user, get_sidebar_riwayat
from app.utils import hitung_aktivitas_sumber

# === KONSTANTA === #
SATUAN_AKTIVITAS = {
    "Bq",
    "kBq",
    "MBq",
    "GBq",
    "TBq",
    "Ci",
    "mCi",
    "uCi",
}

# === DEFAULT FORM === #
def get_default_form_data():
    return {
        "radioisotop": "",
        "aktivitas_awal": "",
        "satuan_awal": "Ci",
        "satuan_hasil": "Ci",
        "tanggal_awal": "",
        "tanggal_hitung": waktu_indonesia().date().strftime("%Y-%m-%d"),
        "keterangan": "",
    }

# === REQUEST FORM === #
def get_form_data_from_request():
    return {
        "radioisotop": request.form.get("radioisotop", "").strip(),
        "aktivitas_awal": request.form.get("aktivitas_awal", "").strip(),
        "satuan_awal": request.form.get("satuan_awal", "Ci").strip(),
        "satuan_hasil": request.form.get("satuan_hasil", "Ci").strip(),
        "tanggal_awal": request.form.get("tanggal_awal", "").strip(),
        "tanggal_hitung": request.form.get("tanggal_hitung", "").strip(),
        "keterangan": request.form.get("keterangan", "").strip(),
    }

# === FORMAT SATUAN === #
def format_satuan_aktivitas(satuan):
    if satuan == "uCi":
        return "µCi"
    return satuan

# === VALIDASI FORM === #
def validasi_form_aktivitas(form_data):
    ...
    
# === PARSE TANGGAL === #
def parse_tanggal(nilai_tanggal, nama_input):
    try:
        return datetime.strptime(nilai_tanggal, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"{nama_input} tidak valid.")


# === ROUTE AKTIVITAS === #
@main_bp.route("/aktivitas", methods=["GET", "POST"])
def aktivitas():

    # === CEK LOGIN === #
    if not session.get("user_id"):
        return redirect(url_for("auth.login"))

    user = get_current_user()
    if not user:
        session.clear()
        return redirect(url_for("auth.login"))

    # === DATA AWAL === #
    sidebar_riwayat = get_sidebar_riwayat(user.id)
    form_data = get_default_form_data()
    hasil = None

    # === PROSES POST === #
    if request.method == "POST":
        try:

            # === VALIDASI INPUT === #
            form_data = get_form_data_from_request()
            validasi_form_aktivitas(form_data)
            
            tanggal_awal = parse_tanggal(form_data["tanggal_awal"], "Tanggal sertifikat sumber")
            tanggal_hitung = parse_tanggal(form_data["tanggal_hitung"], "Tanggal perhitungan")
            if tanggal_hitung < tanggal_awal:
                raise ValueError(
                    "Tanggal perhitungan tidak boleh lebih awal dari tanggal sertifikat sumber."
                )

            # === HITUNG AKTIVITAS === #
            data_hitung = hitung_aktivitas_sumber(
                radioisotop_input=form_data["radioisotop"],
                aktivitas_awal=float(form_data["aktivitas_awal"]),
                satuan_awal=form_data["satuan_awal"],
                satuan_hasil=form_data["satuan_hasil"],
                tanggal_awal=tanggal_awal,
                tanggal_hitung=tanggal_hitung,
            )

            # === HASIL DAN SIMPAN RIWAYAT === #
            hasil = {
                "radioisotop": data_hitung["radioisotop"],

                "aktivitas_awal_input": data_hitung["aktivitas_awal_input"],
                "satuan_awal": data_hitung["satuan_awal"],
                "satuan_awal_display": format_satuan_aktivitas(data_hitung["satuan_awal"]),
                "aktivitas_awal": round(data_hitung["aktivitas_awal"], 4),

                "selang_hari": data_hitung["selang_hari"],
                "waktu_paruh_hari": round(data_hitung["waktu_paruh_hari"], 2),

                "hasil_aktivitas": round(data_hitung["hasil_aktivitas"],3),
                "satuan_hasil": data_hitung["satuan_hasil"],
                "satuan_hasil_display": format_satuan_aktivitas(data_hitung["satuan_hasil"]),

                "tanggal_awal": tanggal_awal.strftime("%d-%m-%Y"),
                "tanggal_hitung": tanggal_hitung.strftime("%d-%m-%Y"),
            }

            riwayat_baru = RiwayatAktivitas(
                user_id=user.id,
                radioisotop=data_hitung["radioisotop"],

                aktivitas_awal_input=data_hitung["aktivitas_awal_input"],
                satuan_awal=data_hitung["satuan_awal"],
                aktivitas_awal=data_hitung["aktivitas_awal"],
                satuan_hasil=data_hitung["satuan_hasil"],

                tanggal_awal=data_hitung["tanggal_awal"],
                tanggal_hitung=data_hitung["tanggal_hitung"],
                selang_hari=data_hitung["selang_hari"],
                waktu_paruh_hari=data_hitung["waktu_paruh_hari"],

                hasil_aktivitas=data_hitung["hasil_aktivitas"],
                keterangan=form_data["keterangan"] or None,
            )


            db.session.add(riwayat_baru)
            db.session.commit()
            sidebar_riwayat = get_sidebar_riwayat(user.id)

            # === FLASH SUCCESS === #
            flash("Perhitungan aktivitas berhasil dan riwayat telah disimpan.", "success")

        # === ERROR VALIDASI === #
        except ValueError as error:
            db.session.rollback()
            flash(str(error), "error")

        # === ERROR SISTEM === #
        except Exception as error:
            db.session.rollback()
            flash(f"Terjadi kesalahan: {str(error)}", "error")


    # ===== RENDER PAGE =====
    return render_template(
        "pages/aktivitas.html",
        user=user,
        username=user.username,
        full_name=user.full_name,
        form_data=form_data,
        hasil=hasil,
        satuan_aktivitas=SATUAN_AKTIVITAS,
        sidebar_riwayat=sidebar_riwayat,
    )