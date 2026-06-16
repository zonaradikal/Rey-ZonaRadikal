FAKTOR_KE_ACUAN = {
    "aktivitas": {
        "Ci": 37000,
        "mCi": 37,
        "uCi": 0.037,
        "Bq": 0.000001,
        "kBq": 0.001,
        "MBq": 1,
        "GBq": 1000,
        "TBq": 1000000,
    },
    "jarak": {
        "m": 1,
        "cm": 0.01,
    },
    "tebal_perisai": {
        "mm": 1,
        "cm": 10,
    },
    "waktu": {
        "hari": 1,
        "jam": 1 / 24,
        "tahun": 365.25,
    },
    "paparan": {
        "mSv/jam": 1,
        "uSv/jam": 0.001,
        "mR/jam": 0.01,
    },
}
SATUAN_DATA = []
for jenis_besaran, satuan_data in FAKTOR_KE_ACUAN.items():
    for satuan_asal, faktor_asal in satuan_data.items():
        for satuan_tujuan, faktor_tujuan in satuan_data.items():
            SATUAN_DATA.append(
                {
                    "jenis_besaran": jenis_besaran,
                    "satuan_asal": satuan_asal,
                    "satuan_tujuan": satuan_tujuan,
                    "faktor_konversi": faktor_asal / faktor_tujuan,
                }
            )
"""
Catatan satuan acuan:
- aktivitas      -> MBq
- jarak          -> m
- tebal_perisai  -> mm
- waktu          -> hari
- paparan        -> mSv/jam
"""