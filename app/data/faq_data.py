FAQ_DATA = [
    # =========================
    # UMUM
    # =========================
    {
        "kategori": "Umum",
        "pertanyaan": "Apa itu Zona Radikal?",
        "jawaban": (
            "Zona Radikal adalah sistem berbasis web yang membantu pengguna melakukan "
            "perhitungan parameter proteksi radiasi dan memberikan rekomendasi awal "
            "terkait daerah pengendalian serta daerah supervisi radiasi."
        ),
        "urutan": 1,
        "is_active": True,
    },
    {
        "kategori": "Umum",
        "pertanyaan": "Apa tujuan penggunaan sistem ini?",
        "jawaban": (
            "Sistem ini digunakan untuk membantu proses evaluasi daerah kerja radiasi, "
            "terutama melalui perhitungan aktivitas sumber, laju paparan, dan klasifikasi "
            "daerah radiasi."
        ),
        "urutan": 2,
        "is_active": True,
    },
    {
        "kategori": "Umum",
        "pertanyaan": "Apakah hasil sistem ini menggantikan keputusan Petugas Proteksi Radiasi?",
        "jawaban": (
            "Tidak. Sistem ini hanya digunakan sebagai alat bantu perhitungan dan "
            "rekomendasi awal. Keputusan akhir tetap memerlukan pengukuran lapangan, "
            "kondisi fasilitas, dan pertimbangan Petugas Proteksi Radiasi atau Pemegang Izin."
        ),
        "dasar_hukum": "Perka BAPETEN No. 4 Tahun 2013 Pasal 7.",
        "urutan": 3,
        "is_active": True,
    },
    {
        "kategori": "Umum",
        "pertanyaan": "Mengapa pengguna perlu login?",
        "jawaban": (
            "Login diperlukan agar hasil perhitungan dan riwayat pengguna tersimpan "
            "pada akun masing-masing, sehingga data tidak tercampur dengan pengguna lain."
        ),
        "urutan": 4,
        "is_active": True,
    },
    {
        "kategori": "Umum",
        "pertanyaan": "Apa fungsi halaman riwayat?",
        "jawaban": (
            "Halaman riwayat digunakan untuk menampilkan kembali hasil perhitungan "
            "aktivitas sumber, laju paparan, dan daerah radiasi yang pernah dilakukan pengguna."
        ),
        "urutan": 5,
        "is_active": True,
    },


    # =========================
    # AKTIVITAS
    # =========================
    {
        "kategori": "Aktivitas",
        "pertanyaan": "Apa yang dimaksud aktivitas sumber?",
        "jawaban": (
            "Aktivitas sumber menunjukkan jumlah inti radioaktif yang mengalami peluruhan "
            "per satuan waktu. Nilai ini digunakan untuk menghitung aktivitas sumber pada "
            "tanggal perhitungan."
        ),
        "dasar_hukum": "Perka BAPETEN No. 7 Tahun 2013 Pasal 1 angka 1.",
        "urutan": 1,
        "is_active": True,
    },
    {
        "kategori": "Aktivitas",
        "pertanyaan": "Data apa saja yang diperlukan untuk menghitung aktivitas saat ini?",
        "jawaban": (
            "Data yang diperlukan adalah jenis radioisotop, aktivitas awal, satuan aktivitas, "
            "tanggal acuan atau tanggal sertifikat sumber, dan tanggal perhitungan."
        ),
        "urutan": 2,
        "is_active": True,
    },
    {
        "kategori": "Aktivitas",
        "pertanyaan": "Mengapa tanggal acuan sumber perlu dimasukkan?",
        "jawaban": (
            "Tanggal acuan digunakan untuk menentukan selang waktu peluruhan dari aktivitas "
            "awal hingga tanggal perhitungan, sehingga aktivitas sumber saat ini dapat dihitung."
        ),
        "urutan": 3,
        "is_active": True,
    },
    {
        "kategori": "Aktivitas",
        "pertanyaan": "Apakah satuan aktivitas harus selalu MBq?",
        "jawaban": (
            "Tidak. Pengguna dapat memasukkan aktivitas dalam satuan Ci, mCi, uCi, Bq, kBq, "
            "MBq, GBq, atau TBq. Sistem akan melakukan konversi satuan sesuai kebutuhan "
            "perhitungan."
        ),
        "urutan": 4,
        "is_active": True,
    },
    {
        "kategori": "Aktivitas",
        "pertanyaan": "Radioisotop apa saja yang tersedia dalam sistem?",
        "jawaban": (
            "Sistem menyediakan pilihan Cobalt-60 (Co-60), Cesium-137 (Cs-137), dan "
            "Iridium-192 (Ir-192) sesuai batasan penelitian."
        ),
        "urutan": 5,
        "is_active": True,
    },


    # =========================
    # PAPARAN
    # =========================
    {
        "kategori": "Paparan",
        "pertanyaan": "Apa yang dimaksud paparan radiasi?",
        "jawaban": (
            "Paparan radiasi adalah penyinaran radiasi yang diterima manusia atau materi, "
            "baik disengaja maupun tidak, yang berasal dari radiasi interna maupun eksterna."
        ),
        "dasar_hukum": "Perka BAPETEN No. 4 Tahun 2013 Pasal 1 angka 11.",
        "urutan": 1,
        "is_active": True,
    },
    {
        "kategori": "Paparan",
        "pertanyaan": "Data apa saja yang diperlukan untuk menghitung laju paparan?",
        "jawaban": (
            "Data yang diperlukan adalah jenis radioisotop, aktivitas sumber, satuan aktivitas, "
            "jarak dari sumber ke titik tinjau, serta data perisai jika perhitungan dilakukan "
            "dengan perisai."
        ),
        "urutan": 2,
        "is_active": True,
    },
    {
        "kategori": "Paparan",
        "pertanyaan": "Apa perbedaan perhitungan tanpa perisai dan dengan perisai?",
        "jawaban": (
            "Perhitungan tanpa perisai menghitung laju paparan langsung dari sumber ke titik "
            "tinjau. Perhitungan dengan perisai memperhitungkan penurunan paparan berdasarkan "
            "jenis material dan ketebalan perisai."
        ),
        "urutan": 3,
        "is_active": True,
    },
    {
        "kategori": "Paparan",
        "pertanyaan": "Mengapa jarak dari sumber perlu dimasukkan?",
        "jawaban": (
            "Jarak diperlukan karena laju paparan berkurang ketika jarak dari sumber semakin "
            "besar. Prinsip ini digunakan dalam perhitungan laju paparan berdasarkan hubungan "
            "kuadrat terbalik."
        ),
        "urutan": 4,
        "is_active": True,
    },
    {
        "kategori": "Paparan",
        "pertanyaan": "Apa fungsi data perisai pada perhitungan paparan?",
        "jawaban": (
            "Data perisai digunakan untuk memperkirakan seberapa besar paparan radiasi dapat "
            "dikurangi oleh material pelindung, seperti timbal, baja, atau beton."
        ),
        "urutan": 5,
        "is_active": True,
    },
    {
        "kategori": "Paparan",
        "pertanyaan": "Mengapa pemantauan paparan diperlukan?",
        "jawaban": (
            "Pemantauan paparan diperlukan untuk memastikan kondisi daerah kerja tetap "
            "terkendali dan tidak menyebabkan potensi penerimaan paparan yang melebihi batas."
        ),
        "dasar_hukum": "Perka BAPETEN No. 4 Tahun 2013 Pasal 25 huruf b.",
        "urutan": 6,
        "is_active": True,
    },


    # =========================
    # DAERAH
    # =========================
    {
        "kategori": "Daerah",
        "pertanyaan": "Apa yang dimaksud daerah pengendalian?",
        "jawaban": (
            "Daerah pengendalian adalah daerah kerja khusus yang memerlukan pengendalian "
            "lebih ketat untuk mengendalikan paparan normal, mencegah penyebaran kontaminasi, "
            "atau membatasi paparan potensial."
        ),
        "dasar_hukum": "Perka BAPETEN No. 4 Tahun 2013 Pasal 1 angka 21.",
        "urutan": 1,
        "is_active": True,
    },
    {
        "kategori": "Daerah",
        "pertanyaan": "Apa yang dimaksud daerah supervisi?",
        "jawaban": (
            "Daerah supervisi adalah daerah kerja di luar daerah pengendalian yang tetap "
            "memerlukan peninjauan terhadap paparan kerja, tetapi tidak memerlukan tindakan "
            "proteksi atau ketentuan keselamatan khusus seperti daerah pengendalian."
        ),
        "dasar_hukum": "Perka BAPETEN No. 4 Tahun 2013 Pasal 1 angka 22.",
        "urutan": 2,
        "is_active": True,
    },
    {
        "kategori": "Daerah",
        "pertanyaan": "Mengapa daerah kerja radiasi perlu dibagi?",
        "jawaban": (
            "Daerah kerja radiasi perlu dibagi agar potensi penerimaan paparan dapat "
            "dikendalikan dan Nilai Batas Dosis tidak terlampaui."
        ),
        "dasar_hukum": "Perka BAPETEN No. 4 Tahun 2013 Pasal 25 huruf a.",
        "urutan": 3,
        "is_active": True,
    },
    {
        "kategori": "Daerah",
        "pertanyaan": "Kapan daerah pengendalian dapat ditetapkan?",
        "jawaban": (
            "Daerah pengendalian dapat ditetapkan jika potensi penerimaan paparan radiasi "
            "melebihi 3/10 NBD pekerja radiasi dan/atau terdapat potensi kontaminasi."
        ),
        "dasar_hukum": "Perka BAPETEN No. 4 Tahun 2013 Pasal 27 ayat (1).",
        "urutan": 4,
        "is_active": True,
    },
    {
        "kategori": "Daerah",
        "pertanyaan": "Kapan daerah supervisi dapat ditetapkan?",
        "jawaban": (
            "Daerah supervisi dapat ditetapkan jika potensi penerimaan paparan radiasi "
            "individu lebih besar dari NBD anggota masyarakat dan kurang dari 3/10 NBD "
            "pekerja radiasi, serta berada dalam kondisi bebas kontaminasi."
        ),
        "dasar_hukum": "Perka BAPETEN No. 4 Tahun 2013 Pasal 29 ayat (1).",
        "urutan": 5,
        "is_active": True,
    },
    {
        "kategori": "Daerah",
        "pertanyaan": "Apa fungsi faktor okupansi dalam penentuan daerah radiasi?",
        "jawaban": (
            "Faktor okupansi digunakan untuk memperkirakan tingkat keberadaan seseorang "
            "pada area yang dievaluasi. Nilai ini membantu sistem memperkirakan potensi "
            "paparan berdasarkan kemungkinan seseorang berada di area tersebut."
        ),
        "urutan": 6,
        "is_active": True,
    },
    {
        "kategori": "Daerah",
        "pertanyaan": "Apa tindakan yang perlu dilakukan pada daerah pengendalian?",
        "jawaban": (
            "Tindakan pada daerah pengendalian meliputi penandaan dan pembatasan daerah, "
            "pemasangan tanda peringatan, pengaturan akses, serta penyediaan peralatan "
            "pemantauan dan perlengkapan proteksi radiasi."
        ),
        "dasar_hukum": "Perka BAPETEN No. 4 Tahun 2013 Pasal 28.",
        "urutan": 7,
        "is_active": True,
    },
    {
        "kategori": "Daerah",
        "pertanyaan": "Apa tindakan yang perlu dilakukan pada daerah supervisi?",
        "jawaban": (
            "Tindakan pada daerah supervisi meliputi penandaan dan pembatasan daerah "
            "dengan tanda yang jelas serta pemasangan tanda pada titik akses masuk "
            "daerah supervisi."
        ),
        "dasar_hukum": "Perka BAPETEN No. 4 Tahun 2013 Pasal 29 ayat (2).",
        "urutan": 8,
        "is_active": True,
    },
]