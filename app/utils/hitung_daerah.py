import math, statistics

from app.utils.konversi import (
    konversi_jarak_ke_meter,
    konversi_paparan_ke_msv_per_jam,
)

NILAI_BATAS_DOSIS = 20.0

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

    batas_pengendalian_tahun = 0.3 * NILAI_BATAS_DOSIS
    batas_supervisi_tahun = 0.05 * NILAI_BATAS_DOSIS
    batas_pengendalian_jam = (batas_pengendalian_tahun / jam_kerja / faktor_okupansi)
    batas_supervisi_jam = (batas_supervisi_tahun / jam_kerja / faktor_okupansi)

    hasil_pengendalian = jarak_acuan_meter * math.sqrt(laju_paparan_msv / batas_pengendalian_jam)
    hasil_supervisi = jarak_acuan_meter * math.sqrt(laju_paparan_msv / batas_supervisi_jam)
    estimasi_dosis_tahun = (laju_paparan_msv * jam_kerja * faktor_okupansi)


    return {
        "pembatas_dosis": NILAI_BATAS_DOSIS,
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

# === POTENSI KONTAMINASI === #
def hitung_potensi_kontaminasi(
    background_1,
    background_2,
    background_3,
    laju_cacah_sampel
):
    background_1 = validasi_nilai_positif(background_1, "Background 1", 0.01, 100000)
    background_2 = validasi_nilai_positif(background_2, "Background 2", 0.01, 100000)
    background_3 = validasi_nilai_positif(background_3, "Background 3", 0.01, 100000)
    laju_cacah_sampel = validasi_nilai_positif(laju_cacah_sampel, "Laju cacah sampel", 0.01, 100000)

    data_background = [
        background_1,
        background_2,
        background_3,
    ]

    rata_rata = statistics.mean(data_background)
    standar_deviasi = statistics.stdev(data_background)
    batas = rata_rata + (3 * standar_deviasi)
    potensi_kontaminasi = laju_cacah_sampel > batas

    return {
        "background_1": background_1,
        "background_2": background_2,
        "background_3": background_3,
        "rata_rata": rata_rata,
        "standar_deviasi": standar_deviasi,
        "batas": batas,
        "laju_cacah_sampel": laju_cacah_sampel,
        "potensi_kontaminasi": potensi_kontaminasi,
    }