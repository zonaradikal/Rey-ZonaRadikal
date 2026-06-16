import math

from app.models import Radioisotop, Perisai
from app.utils.konversi import (
    konversi_aktivitas_ke_mbq,
    konversi_jarak_ke_meter,
    konversi_tebal_ke_mm,
    konversi_paparan,
)


# === KONSTANTA === #
KONDISI_PAPARAN = {
    "tanpa_perisai",
    "dengan_perisai",
}

SATUAN_HASIL_LAJU_PAPARAN = {
    "mSv/jam",
    "uSv/jam",
    "µSv/jam",
    "μSv/jam",
    "mR/jam",
}


# === VALIDASI NILAI === #
def validasi_nilai_positif(
    nilai,
    nama_field,
    nilai_minimum,
    nilai_maksimum
):
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


# === VALIDASI SATUAN PAPARAN === #
def normalisasi_satuan_laju_paparan(satuan):
    satuan = str(satuan or "mSv/jam").strip()
    if satuan in {"µSv/jam", "μSv/jam"}:
        return "uSv/jam"

    return satuan
def validasi_satuan_hasil(satuan_hasil):
    satuan_hasil = normalisasi_satuan_laju_paparan(satuan_hasil)
    if satuan_hasil not in SATUAN_HASIL_LAJU_PAPARAN:
        raise ValueError("Satuan hasil laju paparan tidak valid.")

    return satuan_hasil


# === QUERY DATABASE === #
def cari_data_perisai(radioisotop, material_perisai):
    return Perisai.query.filter_by(
        radioisotop=radioisotop,
        material_perisai=material_perisai
    ).first()


# === PERHITUNGAN LAJU PAPARAN === #
def hitung_laju_paparan(
    kondisi_perisai,
    radioisotop,
    aktivitas,
    satuan_aktivitas,
    jarak,
    satuan_jarak,
    satuan_hasil="mSv/jam",
    material_perisai=None,
    tebal_perisai=None,
    satuan_tebal_perisai=None
):
    kondisi_perisai = str(kondisi_perisai or "").strip()
    radioisotop = str(radioisotop or "").strip()
    satuan_aktivitas = str(satuan_aktivitas or "").strip()
    satuan_jarak = str(satuan_jarak or "").strip()
    satuan_hasil = validasi_satuan_hasil(satuan_hasil)
    satuan_tebal_perisai = str(satuan_tebal_perisai or "").strip()

    if kondisi_perisai not in KONDISI_PAPARAN:
        raise ValueError("Kondisi paparan tidak valid.")

    if not radioisotop:
        raise ValueError("Radioisotop wajib dipilih.")
    if not satuan_aktivitas:
        raise ValueError("Satuan aktivitas wajib dipilih.")
    if not satuan_jarak:
        raise ValueError("Satuan jarak wajib dipilih.")


    aktivitas_input = validasi_nilai_positif(aktivitas, "Aktivitas", 0.001, 500)
    jarak_input = validasi_nilai_positif(jarak, "Jarak", 1, 100)

    data_radioisotop = Radioisotop.query.filter_by(radioisotop=radioisotop).first()
    if not data_radioisotop:
        raise ValueError("Radioisotop tidak valid.")

    konstanta_gamma = data_radioisotop.konstanta_gamma
    satuan_konstanta_gamma = data_radioisotop.satuan_konstanta_gamma
    if konstanta_gamma is None:
        raise ValueError("Data konstanta gamma radioisotop tidak tersedia.")

    try:
        konstanta_gamma = float(konstanta_gamma)
    except (TypeError, ValueError):
        raise ValueError("Data konstanta gamma radioisotop tidak valid.")

    if not math.isfinite(konstanta_gamma) or konstanta_gamma <= 0:
        raise ValueError("Data konstanta gamma radioisotop tidak valid.")

    aktivitas_mbq = konversi_aktivitas_ke_mbq(
        nilai=aktivitas_input,
        satuan_asal=satuan_aktivitas
    )

    jarak_meter = konversi_jarak_ke_meter(
        nilai=jarak_input,
        satuan_asal=satuan_jarak
    )
    if jarak_meter <= 0:
        raise ValueError("Jarak hasil konversi harus lebih dari 0.")

    laju_tanpa_perisai_msv_per_jam = (konstanta_gamma * aktivitas_mbq / (jarak_meter ** 2))
    laju_paparan_msv_per_jam = laju_tanpa_perisai_msv_per_jam

    hvl = None
    satuan_hvl = None
    hvl_mm = None
    tebal_perisai_input = None
    tebal_perisai_mm = None
    jumlah_hvl = None


    if kondisi_perisai == "dengan_perisai":
        if not material_perisai:
            raise ValueError("Material perisai wajib dipilih.")
        if not satuan_tebal_perisai:
            raise ValueError("Satuan tebal perisai wajib dipilih.")

        tebal_perisai_input = validasi_nilai_positif(tebal_perisai, "Tebal perisai", 0.01, 100 )

        perisai = cari_data_perisai(
            radioisotop=radioisotop,
            material_perisai=material_perisai
        )
        if not perisai:
            raise ValueError(
                "Data HVL tidak ditemukan untuk kombinasi radioisotop dan material perisai tersebut."
            )

        tebal_perisai_mm = konversi_tebal_ke_mm(
            nilai=tebal_perisai_input,
            satuan_asal=satuan_tebal_perisai
        )

        hvl = perisai.hvl
        satuan_hvl = perisai.satuan_hvl
        if hvl is None:
            raise ValueError("Data HVL perisai tidak tersedia.")
        try:
            hvl = float(hvl)
        except (TypeError, ValueError):
            raise ValueError("Data HVL perisai tidak valid.")

        hvl_mm = konversi_tebal_ke_mm(
            nilai=hvl,
            satuan_asal=satuan_hvl
        )
        if hvl_mm <= 0:
            raise ValueError("Data HVL perisai tidak valid.")
        jumlah_hvl = tebal_perisai_mm / hvl_mm

        laju_paparan_msv_per_jam = (laju_tanpa_perisai_msv_per_jam * (0.5 ** jumlah_hvl))

    laju_tanpa_perisai = konversi_paparan(
        nilai=laju_tanpa_perisai_msv_per_jam,
        satuan_asal="mSv/jam",
        satuan_tujuan=satuan_hasil
    )

    laju_paparan = konversi_paparan(
        nilai=laju_paparan_msv_per_jam,
        satuan_asal="mSv/jam",
        satuan_tujuan=satuan_hasil
    )


    return {
        "kondisi_perisai": kondisi_perisai,
        "radioisotop": radioisotop,

        "konstanta_gamma": konstanta_gamma,
        "satuan_konstanta_gamma": satuan_konstanta_gamma,
        "aktivitas_input": aktivitas_input,
        "satuan_aktivitas": satuan_aktivitas,
        "aktivitas": aktivitas_mbq,

        "jarak_input": jarak_input,
        "satuan_jarak": satuan_jarak,
        "jarak": jarak_meter,

        "material_perisai": material_perisai,
        "tebal_perisai_input": tebal_perisai_input,
        "satuan_tebal_perisai": (
            satuan_tebal_perisai
            if kondisi_perisai == "dengan_perisai"
            else None
        ),
        "tebal_perisai": tebal_perisai_mm,

        "hvl": hvl,
        "satuan_hvl": satuan_hvl,
        "hvl_mm": hvl_mm,
        "jumlah_hvl": jumlah_hvl,

        "laju_tanpa_perisai_msv_per_jam": laju_tanpa_perisai_msv_per_jam,
        "laju_paparan_msv_per_jam": laju_paparan_msv_per_jam,

        "laju_tanpa_perisai": laju_tanpa_perisai,
        "laju_paparan": laju_paparan,
        "satuan_laju_paparan": satuan_hasil,
    }