-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: zona_radikal
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('5072e1d722aa');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faq`
--

DROP TABLE IF EXISTS `faq`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faq` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kategori` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `pertanyaan` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `jawaban` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `dasar_hukum` text COLLATE utf8mb4_unicode_ci,
  `urutan` int NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_faq_kategori_pertanyaan` (`kategori`,`pertanyaan`),
  KEY `ix_faq_kategori` (`kategori`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faq`
--

LOCK TABLES `faq` WRITE;
/*!40000 ALTER TABLE `faq` DISABLE KEYS */;
INSERT INTO `faq` VALUES (1,'Umum','Apa itu Zona Radikal?','Zona Radikal adalah sistem berbasis web yang membantu pengguna melakukan perhitungan parameter proteksi radiasi dan memberikan rekomendasi awal terkait daerah pengendalian serta daerah supervisi radiasi.',NULL,1,1),(2,'Umum','Apa tujuan penggunaan sistem ini?','Sistem ini digunakan untuk membantu proses evaluasi daerah kerja radiasi, terutama melalui perhitungan aktivitas sumber, laju paparan, dan klasifikasi daerah radiasi.',NULL,2,1),(3,'Umum','Apakah hasil sistem ini menggantikan keputusan Petugas Proteksi Radiasi?','Tidak. Sistem ini hanya digunakan sebagai alat bantu perhitungan dan rekomendasi awal. Keputusan akhir tetap memerlukan pengukuran lapangan, kondisi fasilitas, dan pertimbangan Petugas Proteksi Radiasi atau Pemegang Izin.','Perka BAPETEN No. 4 Tahun 2013 Pasal 7.',3,1),(4,'Umum','Mengapa pengguna perlu login?','Login diperlukan agar hasil perhitungan dan riwayat pengguna tersimpan pada akun masing-masing, sehingga data tidak tercampur dengan pengguna lain.',NULL,4,1),(5,'Umum','Apa fungsi halaman riwayat?','Halaman riwayat digunakan untuk menampilkan kembali hasil perhitungan aktivitas sumber, laju paparan, dan daerah radiasi yang pernah dilakukan pengguna.',NULL,5,1),(6,'Aktivitas','Apa yang dimaksud aktivitas sumber?','Aktivitas sumber menunjukkan jumlah inti radioaktif yang mengalami peluruhan per satuan waktu. Nilai ini digunakan untuk menghitung aktivitas sumber pada tanggal perhitungan.','Perka BAPETEN No. 7 Tahun 2013 Pasal 1 angka 1.',1,1),(7,'Aktivitas','Data apa saja yang diperlukan untuk menghitung aktivitas saat ini?','Data yang diperlukan adalah jenis radioisotop, aktivitas awal, satuan aktivitas, tanggal acuan atau tanggal sertifikat sumber, dan tanggal perhitungan.',NULL,2,1),(8,'Aktivitas','Mengapa tanggal acuan sumber perlu dimasukkan?','Tanggal acuan digunakan untuk menentukan selang waktu peluruhan dari aktivitas awal hingga tanggal perhitungan, sehingga aktivitas sumber saat ini dapat dihitung.',NULL,3,1),(9,'Aktivitas','Apakah satuan aktivitas harus selalu MBq?','Tidak. Pengguna dapat memasukkan aktivitas dalam satuan Ci, mCi, uCi, Bq, kBq, MBq, GBq, atau TBq. Sistem akan melakukan konversi satuan sesuai kebutuhan perhitungan.',NULL,4,1),(10,'Aktivitas','Radioisotop apa saja yang tersedia dalam sistem?','Sistem menyediakan pilihan Cobalt-60 (Co-60), Cesium-137 (Cs-137), dan Iridium-192 (Ir-192) sesuai batasan penelitian.',NULL,5,1),(11,'Paparan','Apa yang dimaksud paparan radiasi?','Paparan radiasi adalah penyinaran radiasi yang diterima manusia atau materi, baik disengaja maupun tidak, yang berasal dari radiasi interna maupun eksterna.','Perka BAPETEN No. 4 Tahun 2013 Pasal 1 angka 11.',1,1),(12,'Paparan','Data apa saja yang diperlukan untuk menghitung laju paparan?','Data yang diperlukan adalah jenis radioisotop, aktivitas sumber, satuan aktivitas, jarak dari sumber ke titik tinjau, serta data perisai jika perhitungan dilakukan dengan perisai.',NULL,2,1),(13,'Paparan','Apa perbedaan perhitungan tanpa perisai dan dengan perisai?','Perhitungan tanpa perisai menghitung laju paparan langsung dari sumber ke titik tinjau. Perhitungan dengan perisai memperhitungkan penurunan paparan berdasarkan jenis material dan ketebalan perisai.',NULL,3,1),(14,'Paparan','Mengapa jarak dari sumber perlu dimasukkan?','Jarak diperlukan karena laju paparan berkurang ketika jarak dari sumber semakin besar. Prinsip ini digunakan dalam perhitungan laju paparan berdasarkan hubungan kuadrat terbalik.',NULL,4,1),(15,'Paparan','Apa fungsi data perisai pada perhitungan paparan?','Data perisai digunakan untuk memperkirakan seberapa besar paparan radiasi dapat dikurangi oleh material pelindung, seperti timbal, baja, atau beton.',NULL,5,1),(16,'Paparan','Mengapa pemantauan paparan diperlukan?','Pemantauan paparan diperlukan untuk memastikan kondisi daerah kerja tetap terkendali dan tidak menyebabkan potensi penerimaan paparan yang melebihi batas.','Perka BAPETEN No. 4 Tahun 2013 Pasal 25 huruf b.',6,1),(17,'Daerah','Apa yang dimaksud daerah pengendalian?','Daerah pengendalian adalah daerah kerja khusus yang memerlukan pengendalian lebih ketat untuk mengendalikan paparan normal, mencegah penyebaran kontaminasi, atau membatasi paparan potensial.','Perka BAPETEN No. 4 Tahun 2013 Pasal 1 angka 21.',1,1),(18,'Daerah','Apa yang dimaksud daerah supervisi?','Daerah supervisi adalah daerah kerja di luar daerah pengendalian yang tetap memerlukan peninjauan terhadap paparan kerja, tetapi tidak memerlukan tindakan proteksi atau ketentuan keselamatan khusus seperti daerah pengendalian.','Perka BAPETEN No. 4 Tahun 2013 Pasal 1 angka 22.',2,1),(19,'Daerah','Mengapa daerah kerja radiasi perlu dibagi?','Daerah kerja radiasi perlu dibagi agar potensi penerimaan paparan dapat dikendalikan dan Nilai Batas Dosis tidak terlampaui.','Perka BAPETEN No. 4 Tahun 2013 Pasal 25 huruf a.',3,1),(20,'Daerah','Kapan daerah pengendalian dapat ditetapkan?','Daerah pengendalian dapat ditetapkan jika potensi penerimaan paparan radiasi melebihi 3/10 NBD pekerja radiasi dan/atau terdapat potensi kontaminasi.','Perka BAPETEN No. 4 Tahun 2013 Pasal 27 ayat (1).',4,1),(21,'Daerah','Kapan daerah supervisi dapat ditetapkan?','Daerah supervisi dapat ditetapkan jika potensi penerimaan paparan radiasi individu lebih besar dari NBD anggota masyarakat dan kurang dari 3/10 NBD pekerja radiasi, serta berada dalam kondisi bebas kontaminasi.','Perka BAPETEN No. 4 Tahun 2013 Pasal 29 ayat (1).',5,1),(22,'Daerah','Apa fungsi faktor okupansi dalam penentuan daerah radiasi?','Faktor okupansi digunakan untuk memperkirakan tingkat keberadaan seseorang pada area yang dievaluasi. Nilai ini membantu sistem memperkirakan potensi paparan berdasarkan kemungkinan seseorang berada di area tersebut.',NULL,6,1),(23,'Daerah','Apa tindakan yang perlu dilakukan pada daerah pengendalian?','Tindakan pada daerah pengendalian meliputi penandaan dan pembatasan daerah, pemasangan tanda peringatan, pengaturan akses, serta penyediaan peralatan pemantauan dan perlengkapan proteksi radiasi.','Perka BAPETEN No. 4 Tahun 2013 Pasal 28.',7,1),(24,'Daerah','Apa tindakan yang perlu dilakukan pada daerah supervisi?','Tindakan pada daerah supervisi meliputi penandaan dan pembatasan daerah dengan tanda yang jelas serta pemasangan tanda pada titik akses masuk daerah supervisi.','Perka BAPETEN No. 4 Tahun 2013 Pasal 29 ayat (2).',8,1);
/*!40000 ALTER TABLE `faq` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `panduan`
--

DROP TABLE IF EXISTS `panduan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `panduan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `kategori` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `judul` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `isi` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `urutan` int NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_panduan_kategori_judul` (`kategori`,`judul`),
  KEY `ix_panduan_kategori` (`kategori`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `panduan`
--

LOCK TABLES `panduan` WRITE;
/*!40000 ALTER TABLE `panduan` DISABLE KEYS */;
INSERT INTO `panduan` VALUES (1,'Umum','Fungsi Zona Radikal','Zona Radikal membantu pengguna melakukan perhitungan parameter proteksi radiasi dan menentukan daerah pengendalian serta daerah supervisi radiasi secara lebih terstruktur.',1,1),(2,'Umum','Dasar Penggunaan Sistem','Sistem ini digunakan sebagai alat bantu berdasarkan prinsip proteksi dan keselamatan radiasi, terutama dalam pembagian daerah kerja radiasi dan evaluasi potensi paparan.',2,1),(3,'Umum','Batasan Penggunaan','Hasil dari sistem tidak menggantikan pengukuran lapangan, pertimbangan profesional Petugas Proteksi Radiasi, maupun kewenangan Pemegang Izin.',3,1),(4,'Umum','Login dan Keamanan Data','Pengguna perlu login agar riwayat perhitungan dapat tersimpan sesuai akun masing-masing dan tidak tercampur dengan pengguna lain.',4,1),(5,'Umum','Riwayat Perhitungan','Halaman riwayat menampilkan hasil perhitungan aktivitas sumber, laju paparan, dan daerah radiasi yang pernah dilakukan pengguna. Riwayat ini dapat digunakan untuk meninjau kembali hasil evaluasi sebelumnya.',5,1),(6,'Aktivitas','Pilih Radioisotop','Pilih radioisotop yang sesuai dengan sumber radiasi yang digunakan. Sistem menyediakan pilihan Co-60, Cs-137, dan Ir-192.',1,1),(7,'Aktivitas','Masukkan Aktivitas Awal','Masukkan aktivitas awal sumber sesuai nilai pada sertifikat sumber, tanggal kalibrasi, atau dokumen acuan yang digunakan.',2,1),(8,'Aktivitas','Pilih Satuan Aktivitas','Pilih satuan aktivitas awal sesuai data yang tersedia, misalnya Ci, mCi, Bq, kBq, MBq, GBq, atau TBq. Sistem akan melakukan konversi satuan sesuai kebutuhan perhitungan.',3,1),(9,'Aktivitas','Pilih Tanggal Acuan','Tanggal sertifikat sumber digunakan sebagai tanggal awal, sedangkan tanggal perhitungan digunakan untuk menentukan aktivitas sumber pada saat evaluasi dilakukan.',4,1),(10,'Aktivitas','Lihat Hasil Aktivitas Saat Ini','Sistem akan menghitung aktivitas sumber saat ini berdasarkan aktivitas awal, waktu paruh radioisotop, dan selang waktu peluruhan.',5,1),(11,'Paparan','Pilih Kondisi Paparan','Pilih tanpa perisai jika paparan dihitung langsung dari sumber, atau dengan perisai jika terdapat material pelindung.',1,1),(12,'Paparan','Masukkan Aktivitas Sumber','Masukkan aktivitas sumber yang akan digunakan untuk menghitung laju paparan. Aktivitas dapat diambil dari hasil perhitungan halaman aktivitas atau dimasukkan langsung oleh pengguna.',2,1),(13,'Paparan','Masukkan Jarak Titik Tinjau','Masukkan jarak antara sumber radiasi dan titik tinjau. Jarak digunakan dalam perhitungan laju paparan berdasarkan prinsip kuadrat terbalik.',3,1),(14,'Paparan','Masukkan Data Perisai','Jika menggunakan perisai, pilih material perisai dan masukkan ketebalannya. Data ini digunakan untuk memperkirakan penurunan laju paparan radiasi.',4,1),(15,'Paparan','Gunakan Hasil Laju Paparan','Hasil laju paparan dapat digunakan sebagai data pendukung untuk evaluasi daerah radiasi atau sebagai acuan perhitungan berikutnya.',5,1),(16,'Daerah','Masukkan Laju Paparan','Masukkan nilai laju paparan sebagai dasar perhitungan potensi paparan pada daerah kerja yang akan dievaluasi.',1,1),(17,'Daerah','Perhatikan Waktu Kerja','Waktu kerja atau waktu paparan digunakan untuk memperkirakan potensi penerimaan paparan pada area yang dievaluasi.',2,1),(18,'Daerah','Masukkan Nilai Batas Dosis','Masukkan nilai batas dosis pekerja radiasi dan anggota masyarakat sesuai acuan evaluasi yang digunakan. Nilai ini menjadi dasar pembanding dalam penentuan daerah pengendalian dan daerah supervisi.',3,1),(19,'Daerah','Masukkan Faktor Okupansi','Faktor okupansi digunakan untuk memperkirakan tingkat keberadaan seseorang pada area yang dievaluasi. Nilai ini membantu sistem memperkirakan potensi paparan berdasarkan kemungkinan seseorang berada di area tersebut selama waktu kerja atau waktu paparan tertentu.',4,1),(20,'Daerah','Lihat Hasil Klasifikasi Daerah','Sistem akan menampilkan hasil perkiraan daerah pengendalian dan daerah supervisi berdasarkan parameter yang dimasukkan pengguna.',5,1),(21,'Daerah','Gunakan Sebagai Alat Bantu','Hasil klasifikasi digunakan sebagai alat bantu evaluasi. Keputusan akhir tetap perlu disesuaikan dengan hasil pengukuran lapangan, kondisi fasilitas, dan pertimbangan Petugas Proteksi Radiasi (PPR).',6,1);
/*!40000 ALTER TABLE `panduan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `perisai`
--

DROP TABLE IF EXISTS `perisai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `perisai` (
  `id` int NOT NULL AUTO_INCREMENT,
  `radioisotop` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `material_perisai` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `hvl` float NOT NULL,
  `satuan_hvl` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_perisai_radioisotop_material` (`radioisotop`,`material_perisai`),
  KEY `ix_perisai_material_perisai` (`material_perisai`),
  KEY `ix_perisai_radioisotop` (`radioisotop`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `perisai`
--

LOCK TABLES `perisai` WRITE;
/*!40000 ALTER TABLE `perisai` DISABLE KEYS */;
INSERT INTO `perisai` VALUES (1,'Co-60','Timbal',12,'mm'),(2,'Co-60','Baja',21,'mm'),(3,'Co-60','Beton',62,'mm'),(4,'Cs-137','Timbal',6.5,'mm'),(5,'Cs-137','Baja',16,'mm'),(6,'Cs-137','Beton',48,'mm'),(7,'Ir-192','Timbal',6,'mm'),(8,'Ir-192','Baja',13,'mm'),(9,'Ir-192','Beton',43,'mm');
/*!40000 ALTER TABLE `perisai` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `radioisotop`
--

DROP TABLE IF EXISTS `radioisotop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `radioisotop` (
  `id` int NOT NULL AUTO_INCREMENT,
  `radioisotop` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `waktu_paruh` float NOT NULL,
  `satuan_waktu_paruh` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `konstanta_gamma` float NOT NULL,
  `satuan_konstanta_gamma` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_radioisotop_radioisotop` (`radioisotop`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `radioisotop`
--

LOCK TABLES `radioisotop` WRITE;
/*!40000 ALTER TABLE `radioisotop` DISABLE KEYS */;
INSERT INTO `radioisotop` VALUES (1,'Co-60',5.2713,'tahun',0.0003703,'mSv.m²/(jam·MBq)'),(2,'Cs-137',30.1671,'tahun',0.0000778,'mSv.m²/(jam·MBq)'),(3,'Ir-192',73.827,'hari',0.0001167,'mSv.m²/(jam·MBq)');
/*!40000 ALTER TABLE `radioisotop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `riwayat_aktivitas`
--

DROP TABLE IF EXISTS `riwayat_aktivitas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `riwayat_aktivitas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `radioisotop` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `aktivitas_awal_input` float NOT NULL,
  `satuan_awal` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `aktivitas_awal` float NOT NULL,
  `satuan_hasil` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tanggal_awal` date NOT NULL,
  `tanggal_hitung` date NOT NULL,
  `selang_hari` int NOT NULL,
  `waktu_paruh_hari` float NOT NULL,
  `hasil_aktivitas` float NOT NULL,
  `keterangan` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_riwayat_aktivitas_radioisotop` (`radioisotop`),
  KEY `ix_riwayat_aktivitas_user_id` (`user_id`),
  CONSTRAINT `riwayat_aktivitas_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `riwayat_aktivitas`
--

LOCK TABLES `riwayat_aktivitas` WRITE;
/*!40000 ALTER TABLE `riwayat_aktivitas` DISABLE KEYS */;
/*!40000 ALTER TABLE `riwayat_aktivitas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `riwayat_daerah_radiasi`
--

DROP TABLE IF EXISTS `riwayat_daerah_radiasi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `riwayat_daerah_radiasi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `pembatas_dosis` float NOT NULL,
  `jam_kerja` float NOT NULL,
  `laju_paparan` float NOT NULL,
  `satuan_paparan` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `laju_paparan_msv` float NOT NULL,
  `jarak_acuan` float NOT NULL,
  `satuan_jarak_acuan` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `faktor_okupansi` float NOT NULL,
  `batas_pengendalian_tahun` float NOT NULL,
  `batas_supervisi_tahun` float NOT NULL,
  `batas_pengendalian_jam` float NOT NULL,
  `batas_supervisi_jam` float NOT NULL,
  `hasil_pengendalian` float NOT NULL,
  `hasil_supervisi` float NOT NULL,
  `estimasi_dosis_tahun` float NOT NULL,
  `keterangan` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_riwayat_daerah_radiasi_user_id` (`user_id`),
  CONSTRAINT `riwayat_daerah_radiasi_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `riwayat_daerah_radiasi`
--

LOCK TABLES `riwayat_daerah_radiasi` WRITE;
/*!40000 ALTER TABLE `riwayat_daerah_radiasi` DISABLE KEYS */;
/*!40000 ALTER TABLE `riwayat_daerah_radiasi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `riwayat_paparan`
--

DROP TABLE IF EXISTS `riwayat_paparan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `riwayat_paparan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `kondisi_perisai` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `radioisotop` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `konstanta_gamma` float NOT NULL,
  `satuan_konstanta_gamma` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `aktivitas_input` float NOT NULL,
  `satuan_aktivitas` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `aktivitas` float NOT NULL,
  `jarak_input` float NOT NULL,
  `satuan_jarak` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `jarak` float NOT NULL,
  `material_perisai` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tebal_perisai_input` float DEFAULT NULL,
  `satuan_tebal_perisai` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tebal_perisai` float DEFAULT NULL,
  `hvl` float DEFAULT NULL,
  `satuan_hvl` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `laju_paparan` float NOT NULL,
  `satuan_laju_paparan` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `keterangan` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_riwayat_paparan_radioisotop` (`radioisotop`),
  KEY `ix_riwayat_paparan_user_id` (`user_id`),
  CONSTRAINT `riwayat_paparan_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `riwayat_paparan`
--

LOCK TABLES `riwayat_paparan` WRITE;
/*!40000 ALTER TABLE `riwayat_paparan` DISABLE KEYS */;
/*!40000 ALTER TABLE `riwayat_paparan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `satuan_konversi`
--

DROP TABLE IF EXISTS `satuan_konversi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `satuan_konversi` (
  `id` int NOT NULL AUTO_INCREMENT,
  `jenis_besaran` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `satuan_asal` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `satuan_tujuan` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `faktor_konversi` float NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq_satuan_konversi` (`jenis_besaran`,`satuan_asal`,`satuan_tujuan`),
  KEY `ix_satuan_konversi_jenis_besaran` (`jenis_besaran`),
  KEY `ix_satuan_konversi_satuan_asal` (`satuan_asal`),
  KEY `ix_satuan_konversi_satuan_tujuan` (`satuan_tujuan`)
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `satuan_konversi`
--

LOCK TABLES `satuan_konversi` WRITE;
/*!40000 ALTER TABLE `satuan_konversi` DISABLE KEYS */;
INSERT INTO `satuan_konversi` VALUES (1,'aktivitas','Ci','Ci',1),(2,'aktivitas','Ci','mCi',1000),(3,'aktivitas','Ci','uCi',1000000),(4,'aktivitas','Ci','Bq',37000000000),(5,'aktivitas','Ci','kBq',37000000),(6,'aktivitas','Ci','MBq',37000),(7,'aktivitas','Ci','GBq',37),(8,'aktivitas','Ci','TBq',0.037),(9,'aktivitas','mCi','Ci',0.001),(10,'aktivitas','mCi','mCi',1),(11,'aktivitas','mCi','uCi',1000),(12,'aktivitas','mCi','Bq',37000000),(13,'aktivitas','mCi','kBq',37000),(14,'aktivitas','mCi','MBq',37),(15,'aktivitas','mCi','GBq',0.037),(16,'aktivitas','mCi','TBq',0.000037),(17,'aktivitas','uCi','Ci',0.000001),(18,'aktivitas','uCi','mCi',0.001),(19,'aktivitas','uCi','uCi',1),(20,'aktivitas','uCi','Bq',37000),(21,'aktivitas','uCi','kBq',37),(22,'aktivitas','uCi','MBq',0.037),(23,'aktivitas','uCi','GBq',0.000037),(24,'aktivitas','uCi','TBq',0.000000037),(25,'aktivitas','Bq','Ci',0.000000000027027),(26,'aktivitas','Bq','mCi',0.000000027027),(27,'aktivitas','Bq','uCi',0.000027027),(28,'aktivitas','Bq','Bq',1),(29,'aktivitas','Bq','kBq',0.001),(30,'aktivitas','Bq','MBq',0.000001),(31,'aktivitas','Bq','GBq',0.000000001),(32,'aktivitas','Bq','TBq',0.000000000001),(33,'aktivitas','kBq','Ci',0.000000027027),(34,'aktivitas','kBq','mCi',0.000027027),(35,'aktivitas','kBq','uCi',0.027027),(36,'aktivitas','kBq','Bq',1000),(37,'aktivitas','kBq','kBq',1),(38,'aktivitas','kBq','MBq',0.001),(39,'aktivitas','kBq','GBq',0.000001),(40,'aktivitas','kBq','TBq',0.000000001),(41,'aktivitas','MBq','Ci',0.000027027),(42,'aktivitas','MBq','mCi',0.027027),(43,'aktivitas','MBq','uCi',27.027),(44,'aktivitas','MBq','Bq',1000000),(45,'aktivitas','MBq','kBq',1000),(46,'aktivitas','MBq','MBq',1),(47,'aktivitas','MBq','GBq',0.001),(48,'aktivitas','MBq','TBq',0.000001),(49,'aktivitas','GBq','Ci',0.027027),(50,'aktivitas','GBq','mCi',27.027),(51,'aktivitas','GBq','uCi',27027),(52,'aktivitas','GBq','Bq',1000000000),(53,'aktivitas','GBq','kBq',1000000),(54,'aktivitas','GBq','MBq',1000),(55,'aktivitas','GBq','GBq',1),(56,'aktivitas','GBq','TBq',0.001),(57,'aktivitas','TBq','Ci',27.027),(58,'aktivitas','TBq','mCi',27027),(59,'aktivitas','TBq','uCi',27027000),(60,'aktivitas','TBq','Bq',1000000000000),(61,'aktivitas','TBq','kBq',1000000000),(62,'aktivitas','TBq','MBq',1000000),(63,'aktivitas','TBq','GBq',1000),(64,'aktivitas','TBq','TBq',1),(65,'jarak','m','m',1),(66,'jarak','m','cm',100),(67,'jarak','cm','m',0.01),(68,'jarak','cm','cm',1),(69,'tebal_perisai','mm','mm',1),(70,'tebal_perisai','mm','cm',0.1),(71,'tebal_perisai','cm','mm',10),(72,'tebal_perisai','cm','cm',1),(73,'waktu','hari','hari',1),(74,'waktu','hari','jam',24),(75,'waktu','hari','tahun',0.00273785),(76,'waktu','jam','hari',0.0416667),(77,'waktu','jam','jam',1),(78,'waktu','jam','tahun',0.000114077),(79,'waktu','tahun','hari',365.25),(80,'waktu','tahun','jam',8766),(81,'waktu','tahun','tahun',1),(82,'paparan','mSv/jam','mSv/jam',1),(83,'paparan','mSv/jam','uSv/jam',1000),(84,'paparan','mSv/jam','mR/jam',100),(85,'paparan','uSv/jam','mSv/jam',0.001),(86,'paparan','uSv/jam','uSv/jam',1),(87,'paparan','uSv/jam','mR/jam',0.1),(88,'paparan','mR/jam','mSv/jam',0.01),(89,'paparan','mR/jam','uSv/jam',10),(90,'paparan','mR/jam','mR/jam',1);
/*!40000 ALTER TABLE `satuan_konversi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_sessions`
--

DROP TABLE IF EXISTS `user_sessions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_sessions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `login_at` datetime NOT NULL,
  `logout_at` datetime DEFAULT NULL,
  `ip_address` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_agent` text COLLATE utf8mb4_unicode_ci,
  `is_online` tinyint(1) NOT NULL,
  `last_activity_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `user_sessions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_sessions`
--

LOCK TABLES `user_sessions` WRITE;
/*!40000 ALTER TABLE `user_sessions` DISABLE KEYS */;
INSERT INTO `user_sessions` VALUES (1,2,'2026-06-16 17:42:21','2026-06-16 17:43:06','127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',0,NULL),(2,2,'2026-06-16 18:02:28','2026-06-16 18:06:33','127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',0,NULL),(3,2,'2026-06-16 18:06:54',NULL,'127.0.0.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',1,'2026-06-16 19:59:28');
/*!40000 ALTER TABLE `user_sessions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `full_name` varchar(150) COLLATE utf8mb4_unicode_ci NOT NULL,
  `username` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password_hash` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `no_sertifikat_ppr` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `role` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_username` (`username`),
  KEY `ix_users_no_sertifikat_ppr` (`no_sertifikat_ppr`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (2,'Administrator Reyna','adminrey','scrypt:32768:8:1$kwM6DXQsoUu9rZBI$6bfd76ef6bf93cbd544dd48e4487ae93797bb439727e871f22c85ef941a1e8a06dc5e19ef30fcc7c7a9f6c5701195a624cba995ef435522b2426c9a219907b6b','2026-06-16 17:07:09','2026-06-16 17:07:09',NULL,'admin','active');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-16 21:12:15
