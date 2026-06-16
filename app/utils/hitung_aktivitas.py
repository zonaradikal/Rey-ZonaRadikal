import math
from datetime import date, datetime

from app.models import Radioisotop
from app.utils.konversi import konversi_aktivitas, konversi_waktu_ke_hari


# === VALIDASI TANGGAL === #
def ubah_ke_tanggal(nilai_tanggal, nama_field):
    if isinstance(nilai_tanggal, datetime):
        return nilai_tanggal.date()

    if isinstance(nilai_tanggal, date):
        return nilai_tanggal

    if nilai_tanggal is None:
        raise ValueError(f"{nama_field} wajib diisi.")

    if isinstance(nilai_tanggal, str):
        nilai_tanggal = nilai_tanggal.strip()
        if not nilai_tanggal:
            raise ValueError(f"{nama_field} wajib diisi.")
        format_tanggal = [
            "%Y-%m-%d",
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%dT%H:%M",
            "%Y-%m-%dT%H:%M:%S",
        ]

        for format_item in format_tanggal:
            try:
                return datetime.strptime(
                    nilai_tanggal,
                    format_item
                ).date()
            except ValueError:
                continue

    raise ValueError(f"{nama_field} tidak valid.")

def validasi_tanggal(tanggal_awal, tanggal_hitung):
    tanggal_awal = ubah_ke_tanggal(tanggal_awal, "Tanggal awal")
    tanggal_hitung = ubah_ke_tanggal(tanggal_hitung, "Tanggal perhitungan")
    
    if tanggal_hitung < tanggal_awal:
        raise ValueError("Tanggal perhitungan tidak boleh lebih awal dari tanggal awal.")

    return tanggal_awal, tanggal_hitung


# === VALIDASI AKTIVITAS === #
def validasi_aktivitas_awal(aktivitas_awal):
    try:
        aktivitas_awal = float(aktivitas_awal)
    except (TypeError, ValueError):
        raise ValueError("Aktivitas awal harus berupa angka.")
    if not math.isfinite(aktivitas_awal):
        raise ValueError("Aktivitas awal tidak valid.")
    if aktivitas_awal < 0.001:
        raise ValueError("Aktivitas awal minimal 0,001.")
    if aktivitas_awal > 500:
        raise ValueError("Aktivitas awal maksimal 500.")
    return aktivitas_awal


# === PERHITUNGAN AKTIVITAS SUMBER === #
def hitung_aktivitas_sumber(
    radioisotop_input,
    aktivitas_awal,
    satuan_awal,
    satuan_hasil,
    tanggal_awal,
    tanggal_hitung
):
    radioisotop_input = str(radioisotop_input or "").strip()
    satuan_awal = str(satuan_awal or "").strip()
    satuan_hasil = str(satuan_hasil or "").strip()

    if not radioisotop_input:
        raise ValueError("Jenis radioisotop wajib dipilih.")
    if not satuan_awal:
        raise ValueError("Satuan awal wajib dipilih.")
    if not satuan_hasil:
        raise ValueError("Satuan hasil wajib dipilih.")


    aktivitas_awal = validasi_aktivitas_awal(aktivitas_awal)
    tanggal_awal, tanggal_hitung = validasi_tanggal(tanggal_awal, tanggal_hitung)

    radioisotop = Radioisotop.query.filter_by(radioisotop=radioisotop_input).first()
    if radioisotop is None:
        raise ValueError("Jenis radioisotop tidak valid.")

    selang_hari = (tanggal_hitung - tanggal_awal).days
    waktu_paruh_hari = konversi_waktu_ke_hari(
        radioisotop.waktu_paruh,
        radioisotop.satuan_waktu_paruh
    )
    if waktu_paruh_hari <= 0:
        raise ValueError("Data waktu paruh radioisotop tidak valid.")

    aktivitas_awal_terkonversi = konversi_aktivitas(
        nilai=aktivitas_awal,
        satuan_asal=satuan_awal,
        satuan_tujuan=satuan_hasil
    )
    faktor_peluruhan = math.pow(0.5, selang_hari / waktu_paruh_hari)
    hasil_aktivitas = (aktivitas_awal_terkonversi * faktor_peluruhan)


    return {
        "radioisotop": radioisotop.radioisotop,

        "aktivitas_awal_input": aktivitas_awal,
        "satuan_awal": satuan_awal,
        "aktivitas_awal": aktivitas_awal_terkonversi,
        "satuan_hasil": satuan_hasil,

        "tanggal_awal": tanggal_awal,
        "tanggal_hitung": tanggal_hitung,
        "selang_hari": selang_hari,
        "waktu_paruh_hari": waktu_paruh_hari,

        "hasil_aktivitas": hasil_aktivitas,
    }