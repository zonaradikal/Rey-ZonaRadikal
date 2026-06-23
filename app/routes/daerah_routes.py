from flask import render_template, redirect, url_for, session, request, flash

from app.extensions import db
from app.models import RiwayatDaerahRadiasi
from app.routes.main_bp import main_bp
from app.routes.helpers import get_current_user, get_sidebar_riwayat
from app.utils import hitung_daerah_radiasi, hitung_potensi_kontaminasi

# === KONSTANTA === #
SATUAN_PAPARAN = {
    "mSv/jam",
    "uSv/jam",
    "µSv/jam",
    "mR/jam",
}

# === DEFAULT FORM === #
def get_default_form_data():
    return {
        "pembatas_dosis": 20.0,
        "jam_kerja": 2000.0,
        "laju_paparan": "",
        "satuan_paparan": "mSv/jam",
        "jarak_acuan": 1.0,
        "faktor_okupansi": 1.0,
        "keterangan": "",
        "background_1": "",
        "background_2": "",
        "background_3": "",
        "laju_cacah_sampel": "",
        "satuan_kontaminasi": "cpm",
    }

# === REQUEST FORM === #
def get_form_data_from_request():
    satuan_paparan = request.form.get(
        "satuan_paparan",
        "mSv/jam"
    ).strip()
    if satuan_paparan == "µSv/jam":
        satuan_paparan = "uSv/jam"

    return {
        "pembatas_dosis": "20",
        "jam_kerja": request.form.get("jam_kerja", "2000").strip(),
        "laju_paparan": request.form.get("laju_paparan", "").strip(),
        "satuan_paparan": request.form.get("satuan_paparan", "mSv/jam").strip(),
        "jarak_acuan": request.form.get("jarak_acuan", "1").strip(),
        "satuan_jarak_acuan": "m",
        "faktor_okupansi": request.form.get("faktor_okupansi", "1").strip(),
        "keterangan": request.form.get("keterangan", "").strip(),
        "background_1": request.form.get("background_1", "").strip(),
        "background_2": request.form.get("background_2", "").strip(),
        "background_3": request.form.get("background_3", "").strip(),
        "laju_cacah_sampel": request.form.get("laju_cacah_sampel", "").strip(),
        "satuan_kontaminasi": request.form.get("satuan_kontaminasi", "cpm").strip(),
    }

# === VALIDASI FORM === #
def validasi_form_daerah(form_data):
    if not form_data["pembatas_dosis"]:
        raise ValueError("Pembatas dosis wajib diisi.")

    if not form_data["jam_kerja"]:
        raise ValueError("Jam kerja wajib diisi.")

    if not form_data["laju_paparan"]:
        raise ValueError("Laju paparan wajib diisi.")

    if not form_data["jarak_acuan"]:
        raise ValueError("Jarak acuan wajib diisi.")

    if not form_data["faktor_okupansi"]:
        raise ValueError("Faktor okupansi wajib diisi.")

    if not form_data["satuan_paparan"]:
        raise ValueError("Satuan laju paparan wajib dipilih.")

    if form_data["satuan_paparan"] not in SATUAN_PAPARAN:
        raise ValueError("Satuan laju paparan tidak valid.")

# === FORMAT SATUAN === #
def format_satuan_paparan(satuan):
    if satuan == "uSv/jam":
        return "µSv/jam"
    return satuan

# === FORMAT HASIL === #
def format_hasil_angka(nilai, satuan="m"):
    if nilai is None:
        return ""
    return f"{round(nilai, 6)} {satuan}"


# === ROUTE DAERAH === #
@main_bp.route("/daerah", methods=["GET", "POST"])
def daerah():

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
    hasil_pengendalian = None
    hasil_supervisi = None
    hasil_kontaminasi = None

    # === PROSES POST === #
    if request.method == "POST":
        try:

            # === VALIDASI INPUT === #
            form_data = get_form_data_from_request()
            aksi = request.form.get("aksi")

            if aksi == "daerah":
                validasi_form_daerah(form_data)
                data_hitung = hitung_daerah_radiasi(
                    jam_kerja=form_data["jam_kerja"],
                    laju_paparan=form_data["laju_paparan"],
                    satuan_paparan=form_data["satuan_paparan"],
                    jarak_acuan=form_data["jarak_acuan"],
                    satuan_jarak_acuan=form_data["satuan_jarak_acuan"],
                    faktor_okupansi=form_data["faktor_okupansi"],
                )

                hasil_pengendalian = data_hitung["hasil_pengendalian"]
                hasil_supervisi = data_hitung["hasil_supervisi"]

                hasil = {
                    "pembatas_dosis": data_hitung["pembatas_dosis"],
                    "jam_kerja": data_hitung["jam_kerja"],
                    "laju_paparan": data_hitung["laju_paparan"],
                    "satuan_paparan": format_satuan_paparan(data_hitung["satuan_paparan"]),
                    "laju_paparan_msv": data_hitung["laju_paparan_msv"],
                    "jarak_acuan": data_hitung["jarak_acuan"],
                    "faktor_okupansi": data_hitung["faktor_okupansi"],
                    "batas_pengendalian_tahun": data_hitung["batas_pengendalian_tahun"],
                    "batas_supervisi_tahun": data_hitung["batas_supervisi_tahun"],
                    "batas_pengendalian_jam": data_hitung["batas_pengendalian_jam"],
                    "batas_supervisi_jam": data_hitung["batas_supervisi_jam"],
                    "hasil_pengendalian": format_hasil_angka(data_hitung["hasil_pengendalian"]),
                    "hasil_supervisi": format_hasil_angka(data_hitung["hasil_supervisi"]),
                    "estimasi_dosis_tahun": data_hitung["estimasi_dosis_tahun"],
                }

                riwayat_baru = RiwayatDaerahRadiasi(
                    user_id=user.id,
                    pembatas_dosis=data_hitung["pembatas_dosis"],
                    jam_kerja=data_hitung["jam_kerja"],
                    laju_paparan=data_hitung["laju_paparan"],
                    satuan_paparan=data_hitung["satuan_paparan"],
                    laju_paparan_msv=data_hitung["laju_paparan_msv"],
                    jarak_acuan=data_hitung["jarak_acuan"],
                    satuan_jarak_acuan=form_data["satuan_jarak_acuan"],
                    faktor_okupansi=data_hitung["faktor_okupansi"],
                    batas_pengendalian_tahun=data_hitung["batas_pengendalian_tahun"],
                    batas_supervisi_tahun=data_hitung["batas_supervisi_tahun"],
                    batas_pengendalian_jam=data_hitung["batas_pengendalian_jam"],
                    batas_supervisi_jam=data_hitung["batas_supervisi_jam"],
                    hasil_pengendalian=data_hitung["hasil_pengendalian"],
                    hasil_supervisi=data_hitung["hasil_supervisi"],
                    estimasi_dosis_tahun=data_hitung["estimasi_dosis_tahun"],
                    keterangan=form_data["keterangan"] or None,
                )

                db.session.add(riwayat_baru)
                db.session.commit()
                sidebar_riwayat = get_sidebar_riwayat(user.id)

                flash("Perhitungan daerah berhasil dan riwayat telah disimpan.", "success")

            elif aksi == "kontaminasi":

                hasil_kontaminasi = hitung_potensi_kontaminasi(
                    background_1=form_data["background_1"],
                    background_2=form_data["background_2"],
                    background_3=form_data["background_3"],
                    laju_cacah_sampel=form_data["laju_cacah_sampel"],
                )

                flash("Perhitungan potensi kontaminasi berhasil.", "success")

        # === ERROR VALIDASI === #
        except ValueError as error:
            db.session.rollback()
            flash(str(error), "error")
            hasil = None
            hasil_pengendalian = None
            hasil_supervisi = None
            hasil_kontaminasi = None

        # === ERROR SISTEM === #
        except Exception as error:
            db.session.rollback()
            flash(f"Terjadi kesalahan: {str(error)}", "error")
            hasil = None
            hasil_pengendalian = None
            hasil_supervisi = None
            hasil_kontaminasi = None

    # === RENDER PAGE === #
    return render_template(
        "pages/daerah.html",
        user=user,
        username=user.username,
        full_name=user.full_name,
        sidebar_riwayat=sidebar_riwayat,
        form_data=form_data,
        hasil=hasil,
        pembatas_dosis=form_data["pembatas_dosis"],
        jam_kerja=form_data["jam_kerja"],
        laju_paparan=form_data["laju_paparan"],
        jarak_acuan=form_data["jarak_acuan"],
        satuan_paparan=form_data["satuan_paparan"],
        faktor_okupansi=form_data["faktor_okupansi"],
        keterangan=form_data["keterangan"],
        hasil_pengendalian=hasil_pengendalian,
        hasil_supervisi=hasil_supervisi,
        satuan_paparan_list=SATUAN_PAPARAN,
        hasil_kontaminasi=hasil_kontaminasi,
        background_1=form_data["background_1"],
        background_2=form_data["background_2"],
        background_3=form_data["background_3"],
        laju_cacah_sampel=form_data["laju_cacah_sampel"],
        satuan_kontaminasi=form_data["satuan_kontaminasi"],
    )