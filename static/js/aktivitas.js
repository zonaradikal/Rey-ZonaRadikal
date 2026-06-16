
function setupAktivitasValidation() {
  const aktivitasInput = document.getElementById("aktivitas_awal");
  const aktivitasInfo = document.getElementById("aktivitasInfo");
  const tanggalAwal = document.getElementById("tanggal_awal");
  const tanggalHitung = document.getElementById("tanggal_hitung");
  const tanggalHitungInfo = document.getElementById("tanggalHitungInfo");

  /* =========================
     VALIDASI AKTIVITAS
  ========================= */
  if (aktivitasInput && aktivitasInfo) {
    const pesanDefault =
      "Masukkan aktivitas pada tanggal sertifikat sumber.";

    function validasiAktivitas() {
      const nilai = parseFloat(aktivitasInput.value);

      if (!aktivitasInput.value.trim()) {
        aktivitasInfo.textContent = pesanDefault;
        return;
      }

      if (isNaN(nilai)) {
        aktivitasInfo.textContent =
          "Aktivitas harus berupa angka.";
        return;
      }

      if (nilai < 0.001) {
        aktivitasInfo.textContent =
          "Aktivitas awal minimal 0,001.";
        return;
      }

      if (nilai > 500) {
        aktivitasInfo.textContent =
          "Aktivitas awal maksimal 500.";
        return;
      }

      aktivitasInfo.textContent = pesanDefault;
    }

    aktivitasInput.addEventListener("input", validasiAktivitas);
    aktivitasInput.addEventListener("blur", validasiAktivitas);
  }

  /* =========================
     VALIDASI TANGGAL
  ========================= */
  if (tanggalAwal && tanggalHitung && tanggalHitungInfo) {

    const pesanDefaultTanggal =
      "Gunakan tanggal saat aktivitas ingin diketahui.";

    function validasiTanggal() {
      tanggalHitungInfo.textContent = pesanDefaultTanggal;

      if (!tanggalAwal.value || !tanggalHitung.value) {
        return;
      }

      if (
        new Date(tanggalHitung.value) <
        new Date(tanggalAwal.value)
      ) {
        tanggalHitungInfo.textContent =
          "Tanggal perhitungan tidak boleh lebih awal dari tanggal awal.";
      }
    }

    tanggalAwal.addEventListener("change", () => {
      tanggalHitung.min = tanggalAwal.value;
      validasiTanggal();
    });

    tanggalHitung.addEventListener("change", validasiTanggal);
  }
}