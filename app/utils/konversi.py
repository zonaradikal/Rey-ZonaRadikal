from app.models import SatuanKonversi

# === KONSTANTA === #
SATUAN_DASAR = {
    "aktivitas": "MBq",
    "jarak": "m",
    "tebal_perisai": "mm",
    "waktu": "hari",
    "paparan": "mSv/jam",
}

ALIAS_SATUAN = {
    "µCi": "uCi",
    "μCi": "uCi",
    "µSv/jam": "uSv/jam",
    "μSv/jam": "uSv/jam",
}


# === NORMALISASI SATUAN === #
def normalisasi_satuan(satuan):
    if satuan is None:
        return None
    satuan = str(satuan).strip()
    return ALIAS_SATUAN.get(satuan, satuan)
def normalisasi_jenis_besaran(jenis_besaran):
    if jenis_besaran is None:
        return None
    return str(jenis_besaran).strip()


# === KONVERSI SATUAN UMUM === #
def konversi_satuan(nilai, jenis_besaran, satuan_asal, satuan_tujuan):
    if nilai is None:
        raise ValueError("Nilai tidak boleh kosong.")

    jenis_besaran = normalisasi_jenis_besaran(jenis_besaran)
    satuan_asal = normalisasi_satuan(satuan_asal)
    satuan_tujuan = normalisasi_satuan(satuan_tujuan)

    if not jenis_besaran:
        raise ValueError("Jenis besaran tidak boleh kosong.")
    if not satuan_asal:
        raise ValueError("Satuan asal tidak boleh kosong.")
    if not satuan_tujuan:
        raise ValueError("Satuan tujuan tidak boleh kosong.")

    try:
        nilai = float(nilai)
    except (TypeError, ValueError):
        raise ValueError("Nilai harus berupa angka.")
    if nilai < 0:
        raise ValueError("Nilai tidak boleh negatif.")
    if satuan_asal == satuan_tujuan:
        return nilai

    data_konversi = SatuanKonversi.query.filter_by(
        jenis_besaran=jenis_besaran,
        satuan_asal=satuan_asal,
        satuan_tujuan=satuan_tujuan
    ).first()
    if data_konversi is not None:
        return nilai * data_konversi.faktor_konversi

    data_konversi_balik = SatuanKonversi.query.filter_by(
        jenis_besaran=jenis_besaran,
        satuan_asal=satuan_tujuan,
        satuan_tujuan=satuan_asal
    ).first()
    if data_konversi_balik is not None:
        if data_konversi_balik.faktor_konversi == 0:
            raise ValueError("Faktor konversi tidak boleh bernilai 0.")
        return nilai / data_konversi_balik.faktor_konversi

    satuan_dasar = SATUAN_DASAR.get(jenis_besaran)
    if (
        satuan_dasar
        and satuan_asal != satuan_dasar
        and satuan_tujuan != satuan_dasar
    ):
        nilai_dasar = konversi_satuan(
            nilai=nilai,
            jenis_besaran=jenis_besaran,
            satuan_asal=satuan_asal,
            satuan_tujuan=satuan_dasar
        )

        return konversi_satuan(
            nilai=nilai_dasar,
            jenis_besaran=jenis_besaran,
            satuan_asal=satuan_dasar,
            satuan_tujuan=satuan_tujuan
        )

    raise ValueError(
        f"Konversi dari {satuan_asal} ke {satuan_tujuan} "
        f"untuk {jenis_besaran} tidak tersedia."
    )


# === KONVERSI AKTIVITAS === #
def konversi_aktivitas(nilai, satuan_asal, satuan_tujuan):
    return konversi_satuan(
        nilai=nilai,
        jenis_besaran="aktivitas",
        satuan_asal=satuan_asal,
        satuan_tujuan=satuan_tujuan
    )
def konversi_aktivitas_ke_mbq(nilai, satuan_asal):
    return konversi_aktivitas(
        nilai=nilai,
        satuan_asal=satuan_asal,
        satuan_tujuan="MBq"
    )
def konversi_aktivitas_ke_bq(nilai, satuan_asal):
    return konversi_aktivitas(
        nilai=nilai,
        satuan_asal=satuan_asal,
        satuan_tujuan="Bq"
    )
def konversi_aktivitas_ke_ci(nilai, satuan_asal):
    return konversi_aktivitas(
        nilai=nilai,
        satuan_asal=satuan_asal,
        satuan_tujuan="Ci"
    )


# === KONVERSI JARAK === #
def konversi_jarak_ke_meter(nilai, satuan_asal):
    return konversi_satuan(
        nilai=nilai,
        jenis_besaran="jarak",
        satuan_asal=satuan_asal,
        satuan_tujuan="m"
    )


# === KONVERSI TEBAL PERISAI === #
def konversi_tebal_ke_mm(nilai, satuan_asal):
    return konversi_satuan(
        nilai=nilai,
        jenis_besaran="tebal_perisai",
        satuan_asal=satuan_asal,
        satuan_tujuan="mm"
    )


# === KONVERSI WAKTU === #
def konversi_waktu_ke_hari(nilai, satuan_asal):
    return konversi_satuan(
        nilai=nilai,
        jenis_besaran="waktu",
        satuan_asal=satuan_asal,
        satuan_tujuan="hari"
    )
def konversi_waktu_ke_jam(nilai, satuan_asal):
    return konversi_satuan(
        nilai=nilai,
        jenis_besaran="waktu",
        satuan_asal=satuan_asal,
        satuan_tujuan="jam"
    )


# === KONVERSI PAPARAN === #
def konversi_paparan(nilai, satuan_asal, satuan_tujuan):
    return konversi_satuan(
        nilai=nilai,
        jenis_besaran="paparan",
        satuan_asal=satuan_asal,
        satuan_tujuan=satuan_tujuan
    )
def konversi_paparan_ke_msv_per_jam(nilai, satuan_asal):
    return konversi_paparan(
        nilai=nilai,
        satuan_asal=satuan_asal,
        satuan_tujuan="mSv/jam"
    )
def konversi_paparan_ke_usv_per_jam(nilai, satuan_asal):
    return konversi_paparan(
        nilai=nilai,
        satuan_asal=satuan_asal,
        satuan_tujuan="uSv/jam"
    )