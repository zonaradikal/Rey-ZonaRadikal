from flask import render_template, redirect, url_for, session, request, flash, jsonify

from app.extensions import db
from app.models import Radioisotop, Perisai, RiwayatPaparan
from app.models.user import waktu_indonesia
from app.routes.main_bp import main_bp
from app.routes.helpers import get_current_user, get_sidebar_riwayat
from app.utils import hitung_laju_paparan

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


# === DEFAULT FORM === #
def get_default_form_data():
    return {
        "kondisi_perisai": "tanpa_perisai",
        "radioisotop": "",
        "konstanta_gamma": "",
        "aktivitas": "",
        "satuan_aktivitas": "MBq",
        "jarak": "",
        "satuan_jarak": "m",
        "satuan_hasil": "mSv/jam",
        "material_perisai": "",
        "tebal_perisai": "",
        "satuan_tebal_perisai": "mm",
        "hvl_info": "",
        "keterangan": "",
    }

# === REQUEST FORM === #
def get_form_data_from_request():
    return {
        "kondisi_perisai": request.form.get("kondisi_perisai", "tanpa_perisai").strip(),
        "radioisotop": request.form.get("radioisotop", "").strip(),
        "konstanta_gamma": "",
        "aktivitas": request.form.get("aktivitas", "").strip(),
        "satuan_aktivitas": request.form.get("satuan_aktivitas", "MBq").strip(),
        "jarak": request.form.get("jarak", "").strip(),
        "satuan_jarak": request.form.get("satuan_jarak", "m").strip(),
        "satuan_hasil": request.form.get("satuan_hasil", "mSv/jam").strip(),
        "material_perisai": request.form.get("material_perisai", "").strip(),
        "tebal_perisai": request.form.get("tebal_perisai", "").strip(),
        "satuan_tebal_perisai": request.form.get("satuan_tebal_perisai", "mm").strip(),
        "hvl_info": "",
        "keterangan": request.form.get("keterangan", "").strip(),
    }


# === VALIDASI ANGKA === #
def validasi_angka_positif(nilai, nama_input):
    try:
        angka = float(nilai)
    except ValueError:
        raise ValueError(f"{nama_input} harus berupa angka.")

    if angka <= 0:
        raise ValueError(f"{nama_input} harus lebih dari 0.")
    return angka

# === VALIDASI FORM === #
def validasi_form_paparan(form_data):
    if form_data["kondisi_perisai"] not in {"tanpa_perisai", "dengan_perisai",}:
        raise ValueError("Kondisi paparan tidak valid.")
    if not form_data["radioisotop"]: 
        raise ValueError("Radioisotop wajib dipilih.")
    if not form_data["aktivitas"]: 
        raise ValueError("Aktivitas sumber wajib diisi.")

    validasi_angka_positif(form_data["aktivitas"], "Aktivitas sumber")
    if form_data["satuan_aktivitas"] not in SATUAN_AKTIVITAS: 
        raise ValueError("Satuan aktivitas tidak valid.")
    if not form_data["jarak"]: 
        raise ValueError("Jarak dari sumber wajib diisi.")

    validasi_angka_positif(form_data["jarak"], "Jarak dari sumber")
    if form_data["satuan_jarak"] not in SATUAN_JARAK: 
        raise ValueError("Satuan jarak tidak valid.")
    if form_data["satuan_hasil"] not in SATUAN_HASIL_PAPARAN: 
        raise ValueError("Satuan hasil laju paparan tidak valid.")

    if form_data["kondisi_perisai"] == "dengan_perisai":
        if not form_data["material_perisai"]: 
            raise ValueError("Material perisai wajib dipilih.")
        if not form_data["tebal_perisai"]: 
            raise ValueError("Tebal perisai wajib diisi.")

        validasi_angka_positif(form_data["tebal_perisai"], "Tebal perisai")
        if form_data["satuan_tebal_perisai"] not in SATUAN_TEBAL_PERISAI:
            raise ValueError("Satuan tebal perisai tidak valid.")


# === FORMAT SATUAN === #
def format_satuan_paparan(satuan):
    if satuan == "uSv/jam":
        return "µSv/jam"
    return satuan

# === FORMAT INFO === #
def format_info_satuan(nilai, satuan):
    if nilai is None or satuan is None:
        return ""
    return f"{nilai} {satuan}"

# === FORMAT KONDISI === #
def format_kondisi_perisai(kondisi_perisai):
    if kondisi_perisai == "dengan_perisai":
        return "Dengan Perisai"
    return "Tanpa Perisai"

# === FORMAT HASIL === #
def format_hasil_angka(nilai, satuan):
    if nilai is None or satuan is None:
        return ""
    return f"{round(nilai, 6)} {format_satuan_paparan(satuan)}"

# === FORMAT NOTASI ILMIAH === #
def format_notasi_ilmiah(nilai):
    if nilai is None:
        return ""
    mantissa, exponent = f"{float(nilai):.3e}".split("e")
    superscript = str.maketrans(
        "0123456789-",
        "⁰¹²³⁴⁵⁶⁷⁸⁹⁻"
    )
    return f"{float(mantissa):g} × 10{str(int(exponent)).translate(superscript)}"

# === API GAMMA === #
@main_bp.route("/paparan/api/gamma/<radioisotop>")
def get_gamma(radioisotop):
    data = Radioisotop.query.filter_by(radioisotop=radioisotop).first()
    if not data:
        return jsonify({"success": False})

    return jsonify({
        "success": True,
        "konstanta_gamma": data.konstanta_gamma,
        "satuan": data.satuan_konstanta_gamma,
    })


# === API HVL === #
@main_bp.route("/paparan/api/hvl/<radioisotop>/<material>")
def get_hvl(radioisotop, material):
    data = Perisai.query.filter_by(
        radioisotop=radioisotop,
        material_perisai=material
    ).first()
    if not data:
        return jsonify({"success": False})

    return jsonify({
        "success": True,
        "hvl": data.hvl,
        "satuan": data.satuan_hvl,
    })


# === ROUTE PAPARAN === #
@main_bp.route("/paparan", methods=["GET", "POST"])
def paparan():

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
            validasi_form_paparan(form_data)
            material_perisai = None
            tebal_perisai = None
            satuan_tebal_perisai = None

            if form_data["kondisi_perisai"] == "dengan_perisai":
                material_perisai = form_data["material_perisai"]
                tebal_perisai = form_data["tebal_perisai"]
                satuan_tebal_perisai = form_data["satuan_tebal_perisai"]

            # === HITUNG PAPARAN === #
            data_hitung = hitung_laju_paparan(
                kondisi_perisai=form_data["kondisi_perisai"],
                radioisotop=form_data["radioisotop"],
                aktivitas=form_data["aktivitas"],
                satuan_aktivitas=form_data["satuan_aktivitas"],
                jarak=form_data["jarak"],
                satuan_jarak=form_data["satuan_jarak"],
                satuan_hasil=form_data["satuan_hasil"],
                material_perisai=material_perisai,
                tebal_perisai=tebal_perisai,
                satuan_tebal_perisai=satuan_tebal_perisai,
            )

            form_data["konstanta_gamma"] = format_info_satuan(
                format_notasi_ilmiah(data_hitung["konstanta_gamma"]),
                data_hitung["satuan_konstanta_gamma"]
            )

            form_data["hvl_info"] = format_info_satuan(
                data_hitung["hvl"],
                data_hitung["satuan_hvl"]
            )

            form_data["material_perisai"] = data_hitung["material_perisai"] or ""
            form_data["satuan_hasil"] = data_hitung["satuan_laju_paparan"]

            # === HASIL DAN SIMPAN RIWAYAT === #
            hasil = {
                "kondisi": format_kondisi_perisai(data_hitung["kondisi_perisai"]),
                "radioisotop": data_hitung["radioisotop"],
                "konstanta_gamma": form_data["konstanta_gamma"],
                "hvl": form_data["hvl_info"],
                "laju_paparan": (
                    f"{round(data_hitung['laju_paparan'], 4)} "
                    f"{format_satuan_paparan(data_hitung['satuan_laju_paparan'])}"
                ),
                "satuan_laju_paparan": data_hitung["satuan_laju_paparan"],
                "tanggal_hitung": waktu_indonesia().strftime("%d-%m-%Y"),
            }

            riwayat_baru = RiwayatPaparan(
                user_id=user.id,
                kondisi_perisai=data_hitung["kondisi_perisai"],
                radioisotop=data_hitung["radioisotop"],
                konstanta_gamma=data_hitung["konstanta_gamma"],
                satuan_konstanta_gamma=data_hitung["satuan_konstanta_gamma"],

                aktivitas_input=data_hitung["aktivitas_input"],
                satuan_aktivitas=data_hitung["satuan_aktivitas"],
                aktivitas=data_hitung["aktivitas"],
                
                jarak_input=data_hitung["jarak_input"],
                satuan_jarak=data_hitung["satuan_jarak"],
                jarak=data_hitung["jarak"],
                
                material_perisai=data_hitung["material_perisai"],
                tebal_perisai_input=data_hitung["tebal_perisai_input"],
                satuan_tebal_perisai=data_hitung["satuan_tebal_perisai"],
                tebal_perisai=data_hitung["tebal_perisai"],
                hvl=data_hitung["hvl"],
                satuan_hvl=data_hitung["satuan_hvl"],

                laju_paparan=data_hitung["laju_paparan"],
                satuan_laju_paparan=data_hitung["satuan_laju_paparan"],
                keterangan=form_data["keterangan"] or None,
                created_at=waktu_indonesia()
            )

            db.session.add(riwayat_baru)
            db.session.commit()

            sidebar_riwayat = get_sidebar_riwayat(user.id)

            # === FLASH SUCCESS === #
            flash("Perhitungan paparan berhasil dan riwayat telah disimpan.", "success")

        # === ERROR VALIDASI === #
        except ValueError as error:
            db.session.rollback()
            flash(str(error), "error")

        # === ERROR SISTEM === #
        except Exception as error:
            db.session.rollback()
            flash(f"Terjadi kesalahan: {str(error)}", "error")


    # === RENDER PAGE === #
    return render_template(
        "pages/paparan.html",
        user=user,
        username=user.username,
        full_name=user.full_name,
        form_data=form_data,
        hasil=hasil,
        satuan_aktivitas=SATUAN_AKTIVITAS,
        satuan_jarak=SATUAN_JARAK,
        satuan_tebal_perisai=SATUAN_TEBAL_PERISAI,
        satuan_hasil_paparan=SATUAN_HASIL_PAPARAN,
        sidebar_riwayat=sidebar_riwayat,
    )