PANDUAN_DATA = [
    # =========================
    # UMUM
    # =========================
    {
        "kategori": "Umum",
        "judul": "Fungsi Zona Radikal",
        "isi": (
            "Zona Radikal membantu pengguna melakukan perhitungan parameter "
            "proteksi radiasi dan menentukan daerah pengendalian serta daerah "
            "supervisi radiasi secara lebih terstruktur."
        ),
        "urutan": 1,
        "is_active": True,
    },
    {
        "kategori": "Umum",
        "judul": "Dasar Penggunaan Sistem",
        "isi": (
            "Sistem ini digunakan sebagai alat bantu berdasarkan prinsip proteksi "
            "dan keselamatan radiasi, terutama dalam pembagian daerah kerja radiasi "
            "dan evaluasi potensi paparan."
        ),
        "urutan": 2,
        "is_active": True,
    },
    {
        "kategori": "Umum",
        "judul": "Batasan Penggunaan",
        "isi": (
            "Hasil dari sistem tidak menggantikan pengukuran lapangan, pertimbangan "
            "profesional Petugas Proteksi Radiasi, maupun kewenangan Pemegang Izin."
        ),
        "urutan": 3,
        "is_active": True,
    },
    {
        "kategori": "Umum",
        "judul": "Login dan Keamanan Data",
        "isi": (
            "Pengguna perlu login agar riwayat perhitungan dapat tersimpan sesuai "
            "akun masing-masing dan tidak tercampur dengan pengguna lain."
        ),
        "urutan": 4,
        "is_active": True,
    },
    {
        "kategori": "Umum",
        "judul": "Riwayat Perhitungan",
        "isi": (
            "Halaman riwayat menampilkan hasil perhitungan aktivitas sumber, laju "
            "paparan, dan daerah radiasi yang pernah dilakukan pengguna. Riwayat ini "
            "dapat digunakan untuk meninjau kembali hasil evaluasi sebelumnya."
        ),
        "urutan": 5,
        "is_active": True,
    },


    # =========================
    # AKTIVITAS
    # =========================
    {
        "kategori": "Aktivitas",
        "judul": "Pilih Radioisotop",
        "isi": (
            "Pilih radioisotop yang sesuai dengan sumber radiasi yang digunakan. "
            "Sistem menyediakan pilihan Co-60, Cs-137, dan Ir-192."
        ),
        "urutan": 1,
        "is_active": True,
    },
    {
        "kategori": "Aktivitas",
        "judul": "Masukkan Aktivitas Awal",
        "isi": (
            "Masukkan aktivitas awal sumber sesuai nilai pada sertifikat sumber, "
            "tanggal kalibrasi, atau dokumen acuan yang digunakan."
        ),
        "urutan": 2,
        "is_active": True,
    },
    {
        "kategori": "Aktivitas",
        "judul": "Pilih Satuan Aktivitas",
        "isi": (
            "Pilih satuan aktivitas awal sesuai data yang tersedia, misalnya Ci, mCi, "
            "Bq, kBq, MBq, GBq, atau TBq. Sistem akan melakukan konversi satuan "
            "sesuai kebutuhan perhitungan."
        ),
        "urutan": 3,
        "is_active": True,
    },
    {
        "kategori": "Aktivitas",
        "judul": "Pilih Tanggal Acuan",
        "isi": (
            "Tanggal sertifikat sumber digunakan sebagai tanggal awal, sedangkan "
            "tanggal perhitungan digunakan untuk menentukan aktivitas sumber pada "
            "saat evaluasi dilakukan."
        ),
        "urutan": 4,
        "is_active": True,
    },
    {
        "kategori": "Aktivitas",
        "judul": "Lihat Hasil Aktivitas Saat Ini",
        "isi": (
            "Sistem akan menghitung aktivitas sumber saat ini berdasarkan aktivitas "
            "awal, waktu paruh radioisotop, dan selang waktu peluruhan."
        ),
        "urutan": 5,
        "is_active": True,
    },


    # =========================
    # PAPARAN
    # =========================
    {
        "kategori": "Paparan",
        "judul": "Pilih Kondisi Paparan",
        "isi": (
            "Pilih tanpa perisai jika paparan dihitung langsung dari sumber, atau "
            "dengan perisai jika terdapat material pelindung."
        ),
        "urutan": 1,
        "is_active": True,
    },
    {
        "kategori": "Paparan",
        "judul": "Masukkan Aktivitas Sumber",
        "isi": (
            "Masukkan aktivitas sumber yang akan digunakan untuk menghitung laju "
            "paparan. Aktivitas dapat diambil dari hasil perhitungan halaman aktivitas "
            "atau dimasukkan langsung oleh pengguna."
        ),
        "urutan": 2,
        "is_active": True,
    },
    {
        "kategori": "Paparan",
        "judul": "Masukkan Jarak Titik Tinjau",
        "isi": (
            "Masukkan jarak antara sumber radiasi dan titik tinjau. Jarak digunakan "
            "dalam perhitungan laju paparan berdasarkan prinsip kuadrat terbalik."
        ),
        "urutan": 3,
        "is_active": True,
    },
    {
        "kategori": "Paparan",
        "judul": "Masukkan Data Perisai",
        "isi": (
            "Jika menggunakan perisai, pilih material perisai dan masukkan ketebalannya. "
            "Data ini digunakan untuk memperkirakan penurunan laju paparan radiasi."
        ),
        "urutan": 4,
        "is_active": True,
    },
    {
        "kategori": "Paparan",
        "judul": "Gunakan Hasil Laju Paparan",
        "isi": (
            "Hasil laju paparan dapat digunakan sebagai data pendukung untuk evaluasi "
            "daerah radiasi atau sebagai acuan perhitungan berikutnya."
        ),
        "urutan": 5,
        "is_active": True,
    },


    # =========================
    # DAERAH
    # =========================
    {
        "kategori": "Daerah",
        "judul": "Masukkan Laju Paparan",
        "isi": (
            "Masukkan nilai laju paparan sebagai dasar perhitungan potensi paparan "
            "pada daerah kerja yang akan dievaluasi."
        ),
        "urutan": 1,
        "is_active": True,
    },
    {
        "kategori": "Daerah",
        "judul": "Perhatikan Waktu Kerja",
        "isi": (
            "Waktu kerja atau waktu paparan digunakan untuk memperkirakan potensi "
            "penerimaan paparan pada area yang dievaluasi."
        ),
        "urutan": 2,
        "is_active": True,
    },
    {
        "kategori": "Daerah",
        "judul": "Masukkan Nilai Batas Dosis",
        "isi": (
            "Masukkan nilai batas dosis pekerja radiasi dan anggota masyarakat sesuai "
            "acuan evaluasi yang digunakan. Nilai ini menjadi dasar pembanding dalam "
            "penentuan daerah pengendalian dan daerah supervisi."
        ),
        "urutan": 3,
        "is_active": True,
    },
    {
        "kategori": "Daerah",
        "judul": "Masukkan Faktor Okupansi",
        "isi": (
            "Faktor okupansi digunakan untuk memperkirakan tingkat keberadaan seseorang "
            "pada area yang dievaluasi. Nilai ini membantu sistem memperkirakan potensi "
            "paparan berdasarkan kemungkinan seseorang berada di area tersebut selama "
            "waktu kerja atau waktu paparan tertentu."
        ),
        "urutan": 4,
        "is_active": True,
    }, 
    {
        "kategori": "Daerah",
        "judul": "Lihat Hasil Klasifikasi Daerah",
        "isi": (
            "Sistem akan menampilkan hasil perkiraan daerah pengendalian dan daerah "
            "supervisi berdasarkan parameter yang dimasukkan pengguna."
        ),
        "urutan": 5,
        "is_active": True,
    },
    {
        "kategori": "Daerah",
        "judul": "Gunakan Sebagai Alat Bantu",
        "isi": (
            "Hasil klasifikasi digunakan sebagai alat bantu evaluasi. Keputusan akhir "
            "tetap perlu disesuaikan dengan hasil pengukuran lapangan, kondisi fasilitas, "
            "dan pertimbangan Petugas Proteksi Radiasi (PPR)."
        ),
        "urutan": 6,
        "is_active": True,
    },
]