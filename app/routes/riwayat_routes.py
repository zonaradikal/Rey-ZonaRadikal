from flask import render_template, redirect, url_for, session, flash

from app.models import (RiwayatAktivitas, RiwayatPaparan, RiwayatDaerahRadiasi,)
from app.models.user import waktu_indonesia
from app.routes.main_bp import main_bp
from app.routes.helpers import (get_current_user, get_sidebar_riwayat, get_all_riwayat,)

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

SATUAN_JARAK = {
    "m",
    "cm",
}

SATUAN_TEBAL_PERISAI = {
    "mm",
    "cm",
}

SATUAN_HASIL_PAPARAN = {
    "mSv/jam",
    "uSv/jam",
    "mR/jam",
}

SATUAN_PAPARAN_DAERAH = {
    "mSv/jam",
    "uSv/jam",
    "µSv/jam",
    "mR/jam",
}


# === FORMAT TANGGAL === #
def format_tanggal(nilai_tanggal):
    if not nilai_tanggal:
        return ""
    return nilai_tanggal.strftime("%Y-%m-%d")

# === FORMAT SATUAN === #
def format_info_satuan(nilai, satuan):
    if nilai is None or satuan is None:
        return ""
    return f"{nilai} {satuan}"

# === LOGIN === #
def pastikan_user_login():
    if not session.get("user_id"):
        return None, redirect(url_for("auth.login"))
    user = get_current_user()
    if not user:
        session.clear()
        return None, redirect(url_for("auth.login"))

    return user, None


# === ROUTE RIWAYAT === #
@main_bp.route("/riwayat")
def riwayat():

    # === CEK LOGIN === #
    user, redirect_response = pastikan_user_login()
    if redirect_response:
        return redirect_response

    # === DATA AWAL === #
    riwayat_aktivitas = RiwayatAktivitas.query.filter_by(user_id=user.id).order_by(
        RiwayatAktivitas.created_at.desc()).all()
    riwayat_paparan = RiwayatPaparan.query.filter_by(user_id=user.id).order_by(
        RiwayatPaparan.created_at.desc()).all()
    riwayat_daerah = RiwayatDaerahRadiasi.query.filter_by(user_id=user.id).order_by(
        RiwayatDaerahRadiasi.created_at.desc()).all()
    data_riwayat = get_all_riwayat(user.id)
    sidebar_riwayat = get_sidebar_riwayat(user.id)

    # === RENDER PAGE === #
    return render_template(
        "pages/riwayat.html",
        user=user,
        username=user.username,
        full_name=user.full_name,
        data_riwayat=data_riwayat,
        riwayat_aktivitas=riwayat_aktivitas,
        riwayat_paparan=riwayat_paparan,
        riwayat_daerah=riwayat_daerah,
        sidebar_riwayat=sidebar_riwayat,
    )


# === ROUTE GUNAKAN RIWAYAT === #
@main_bp.route("/riwayat/gunakan/<string:jenis>/<int:riwayat_id>")
def gunakan_riwayat(jenis, riwayat_id):

    # === CEK LOGIN === #
    user, redirect_response = pastikan_user_login()
    if redirect_response:
        return redirect_response

    # === DATA AWAL === #
    sidebar_riwayat = get_sidebar_riwayat(user.id)


    # === RIWAYAT AKTIVITAS === #
    if jenis == "aktivitas":
        data = RiwayatAktivitas.query.filter_by(id=riwayat_id, user_id=user.id).first()
        if not data:
            flash("Data riwayat aktivitas tidak ditemukan.", "error")
            return redirect(url_for("main.riwayat"))

        form_data = {
            "radioisotop": data.radioisotop,
            "aktivitas_awal": data.aktivitas_awal_input,
            "satuan_awal": data.satuan_awal,
            "satuan_hasil": data.satuan_hasil,
            "tanggal_awal": format_tanggal(data.tanggal_awal),
            "tanggal_hitung": waktu_indonesia().date().strftime("%Y-%m-%d"),
            "keterangan": data.keterangan or "-",
        }

        return render_template(
            "pages/aktivitas.html",
            user=user,
            username=user.username,
            full_name=user.full_name,
            form_data=form_data,
            hasil=None,
            satuan_aktivitas=SATUAN_AKTIVITAS,
            sidebar_riwayat=sidebar_riwayat,
        )


    # === RIWAYAT PAPARAN === #
    if jenis == "paparan":
        data = RiwayatPaparan.query.filter_by(id=riwayat_id, user_id=user.id).first()
        if not data:
            flash("Data riwayat paparan tidak ditemukan.", "error")
            return redirect(url_for("main.riwayat"))

        form_data = {
            "kondisi_perisai": data.kondisi_perisai,
            "radioisotop": data.radioisotop,
            "konstanta_gamma": format_info_satuan(data.konstanta_gamma, data.satuan_konstanta_gamma),
            "aktivitas": data.aktivitas_input,
            "satuan_aktivitas": data.satuan_aktivitas,
            "jarak": data.jarak_input,
            "satuan_jarak": data.satuan_jarak,
            "satuan_hasil": data.satuan_laju_paparan,
            "material_perisai": (data.material_perisai or ""),
            "tebal_perisai": (data.tebal_perisai_input or ""),
            "satuan_tebal_perisai": (data.satuan_tebal_perisai or "mm"),
            "hvl_info": format_info_satuan(data.hvl, data.satuan_hvl),
            "keterangan": data.keterangan or "",
        }

        return render_template(
            "pages/paparan.html",
            user=user,
            username=user.username,
            full_name=user.full_name,
            form_data=form_data,
            hasil=None,
            satuan_aktivitas=SATUAN_AKTIVITAS,
            satuan_jarak=SATUAN_JARAK,
            satuan_tebal_perisai=SATUAN_TEBAL_PERISAI,
            satuan_hasil_paparan=SATUAN_HASIL_PAPARAN,
            sidebar_riwayat=sidebar_riwayat,
        )


    # === RIWAYAT DAERAH === #
    if jenis == "daerah":
        data = RiwayatDaerahRadiasi.query.filter_by(id=riwayat_id, user_id=user.id).first()
        if not data:
            flash("Data riwayat daerah tidak ditemukan.", "error")
            return redirect(url_for("main.riwayat"))

        form_data = {
            "pembatas_dosis": data.pembatas_dosis,
            "jam_kerja": data.jam_kerja,
            "laju_paparan": data.laju_paparan,
            "satuan_paparan": data.satuan_paparan,
            "jarak_acuan": data.jarak_acuan,
            "satuan_jarak_acuan": data.satuan_jarak_acuan,
            "faktor_okupansi": data.faktor_okupansi,
            "keterangan": data.keterangan or "-",
        }
        
        return render_template(
            "pages/daerah.html",
            user=user,
            username=user.username,
            full_name=user.full_name,
            sidebar_riwayat=sidebar_riwayat,
            form_data=form_data,
            hasil=None,
            
            pembatas_dosis=form_data["pembatas_dosis"],
            jam_kerja=form_data["jam_kerja"],
            
            laju_paparan=form_data["laju_paparan"],
            jarak_acuan=form_data["jarak_acuan"],
            satuan_paparan=form_data["satuan_paparan"],
            
            faktor_okupansi=form_data["faktor_okupansi"],
            keterangan=form_data["keterangan"],
            
            hasil_pengendalian=None,
            hasil_supervisi=None,
            satuan_paparan_list=SATUAN_PAPARAN_DAERAH,
        )

    # === ERROR JENIS RIWAYAT === #
    flash("Jenis riwayat tidak dikenali.", "error")
    return redirect(url_for("main.riwayat"))