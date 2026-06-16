import math

from app.utils.konversi import (
    konversi_jarak_ke_meter,
    konversi_paparan_ke_msv_per_jam,
)


# === VALIDASI NILAI === #
def validasi_nilai_positif(nilai, nama_field, nilai_minimum, nilai_maksimum):
    try:
        nilai = float(nilai)
    except (TypeError, ValueError):
        raise ValueError(f"{nama_field} harus berupa angka.")
    if not math.isfinite(nilai):
        raise ValueError(f"{nama_field} tidak valid.")
    if nilai < nilai_minimum:
        raise ValueError(
            f"{nama_field} minimal {nilai_minimum}."
        )
    if nilai > nilai_maksimum:
        raise ValueError(
            f"{nama_field} maksimal {nilai_maksimum}."
        )
    
    return nilai


# === VALIDASI FAKTOR OKUPANSI === #
def validasi_faktor_okupansi(faktor_okupansi):
    return validasi_nilai_positif (faktor_okupansi, "Faktor okupansi", 0.01, 1)


# === PERHITUNGAN DAERAH RADIASI === #
def hitung_daerah_radiasi(
    pembatas_dosis,
    jam_kerja,
    laju_paparan,
    satuan_paparan,
    jarak_acuan,
    satuan_jarak_acuan,
    faktor_okupansi
):
    satuan_paparan = str(satuan_paparan or "").strip()
    if not satuan_paparan:
        raise ValueError("Satuan laju paparan wajib dipilih.")

    pembatas_dosis = validasi_nilai_positif(pembatas_dosis, "Pembatas dosis", 1, 100)
    jam_kerja = validasi_nilai_positif(jam_kerja, "Jam kerja", 1, 5000)
    laju_paparan = validasi_nilai_positif(laju_paparan, "Laju paparan", 0.001, 500)
    jarak_acuan = validasi_nilai_positif(jarak_acuan, "Jarak acuan", 1, 100)

    jarak_acuan_meter = konversi_jarak_ke_meter(
        nilai=jarak_acuan,
        satuan_asal=satuan_jarak_acuan
    )

    faktor_okupansi = validasi_faktor_okupansi(faktor_okupansi)

    laju_paparan_msv = konversi_paparan_ke_msv_per_jam(
        laju_paparan,
        satuan_paparan
    )
    if laju_paparan_msv <= 0:
        raise ValueError("Laju paparan hasil konversi harus lebih dari 0.")

    batas_pengendalian_tahun = 0.3 * pembatas_dosis
    batas_supervisi_tahun = 0.05 * pembatas_dosis
    batas_pengendalian_jam = (batas_pengendalian_tahun / jam_kerja / faktor_okupansi)
    batas_supervisi_jam = (batas_supervisi_tahun / jam_kerja / faktor_okupansi)

    hasil_pengendalian = jarak_acuan_meter * math.sqrt(laju_paparan_msv / batas_pengendalian_jam)
    hasil_supervisi = jarak_acuan_meter * math.sqrt(laju_paparan_msv / batas_supervisi_jam)
    estimasi_dosis_tahun = (laju_paparan_msv * jam_kerja * faktor_okupansi)


    return {
        "pembatas_dosis": pembatas_dosis,
        "jam_kerja": jam_kerja,
        "laju_paparan": laju_paparan,
        "satuan_paparan": satuan_paparan,
        "laju_paparan_msv": laju_paparan_msv,
        "jarak_acuan": jarak_acuan_meter,
        "faktor_okupansi": faktor_okupansi,

        "batas_pengendalian_tahun": batas_pengendalian_tahun,
        "batas_supervisi_tahun": batas_supervisi_tahun,
        "batas_pengendalian_jam": batas_pengendalian_jam,
        "batas_supervisi_jam": batas_supervisi_jam,

        "hasil_pengendalian": hasil_pengendalian,
        "hasil_supervisi": hasil_supervisi,
        "estimasi_dosis_tahun": estimasi_dosis_tahun,
        "satuan_hasil": "m",
    }