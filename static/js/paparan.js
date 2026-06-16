
const aktivitasInput = document.getElementById("aktivitas");
const jarakInput = document.getElementById("jarak");
const tebalPerisaiInput = document.getElementById("tebal_perisai");

const aktivitasInfo = document.getElementById("aktivitasInfo");
const jarakInfo = document.getElementById("jarakInfo");
const tebalPerisaiInfo = document.getElementById("tebalPerisaiInfo");

/* =========================
   VALIDASI AKTIVITAS
========================= */
function validasiAktivitas() {
  if (!aktivitasInput || !aktivitasInfo) {
    return;
  }

  const nilai = parseFloat(aktivitasInput.value);

  aktivitasInfo.textContent =
    "Masukkan aktivitas sumber yang akan digunakan.";

  if (!aktivitasInput.value) {
    return;
  }

  if (isNaN(nilai)) {
    aktivitasInfo.textContent =
      "Aktivitas harus berupa angka.";
    return;
  }

  if (nilai < 0.001) {
    aktivitasInfo.textContent =
      "Aktivitas minimal 0,001.";
    return;
  }

  if (nilai > 500) {
    aktivitasInfo.textContent =
      "Aktivitas maksimal 500.";
  }
}

/* =========================
   VALIDASI JARAK
========================= */
function validasiJarak() {
  if (!jarakInput || !jarakInfo) {
    return;
  }

  const nilai = parseFloat(jarakInput.value);

  jarakInfo.textContent =
    "Gunakan jarak dari sumber radiasi ke titik tinjau.";

  if (!jarakInput.value) {
    return;
  }

  if (isNaN(nilai)) {
    jarakInfo.textContent =
      "Jarak harus berupa angka.";
    return;
  }

  if (nilai < 1) {
    jarakInfo.textContent =
      "Jarak minimal 1.";
    return;
  }

  if (nilai > 100) {
    jarakInfo.textContent =
      "Jarak maksimal 100.";
  }
}

/* =========================
   VALIDASI TEBAL PERISAI
========================= */
function validasiTebalPerisai() {
  if (!tebalPerisaiInput || !tebalPerisaiInfo) {
    return;
  }

  const nilai = parseFloat(tebalPerisaiInput.value);

  tebalPerisaiInfo.textContent =
    "Masukkan tebal perisai yang digunakan.";

  if (!tebalPerisaiInput.value) {
    return;
  }

  if (isNaN(nilai)) {
    tebalPerisaiInfo.textContent =
      "Tebal perisai harus berupa angka.";
    return;
  }

  if (nilai <= 0) {
    tebalPerisaiInfo.textContent =
      "Tebal perisai harus lebih dari 0.";
  }
}

/* =========================
   PAPARAN FORM
========================= */
function setupPaparanForm() {
  const kondisiInputs = document.querySelectorAll('input[name="kondisi_perisai"]');
  const sectionPerisai = document.getElementById("section-perisai");

  const radioisotopSelect = document.getElementById("radioisotop");
  const materialPerisaiSelect = document.getElementById("material_perisai");

  const konstantaGammaInput = document.getElementById("konstanta_gamma");
  const hvlInfoInput = document.getElementById("hvl_info");

  if (!kondisiInputs.length) {
    return;
  }

  /* =========================
     TOGGLE PERISAI
  ========================= */
  function togglePerisai() {
    const kondisi = document.querySelector('input[name="kondisi_perisai"]:checked')?.value;

    if (!sectionPerisai) {
      return;
    }

    sectionPerisai.style.display =
      kondisi === "dengan_perisai"
        ? "block"
        : "none";
  }

  /* =========================
     UPDATE GAMMA
  ========================= */
  async function updateGamma() {
    if (!radioisotopSelect || !konstantaGammaInput) {
      return;
    }

    const radioisotop = radioisotopSelect.value;

    if (!radioisotop) {
      konstantaGammaInput.value = "";
      return;
    }

    try {
      const data = await fetchJSON(
        `/paparan/api/gamma/${encodeURIComponent(radioisotop)}`
      );

      if (data.success) {
        konstantaGammaInput.value =
          `${data.konstanta_gamma} ${data.satuan}`;
      } else {
        konstantaGammaInput.value = "";
      }

    } catch (error) {

      handleError(error);

      konstantaGammaInput.value = "";
    }
  }

  /* =========================
     UPDATE HVL
  ========================= */
  async function updateHVL() {
    if (
      !radioisotopSelect ||
      !materialPerisaiSelect ||
      !hvlInfoInput
    ) {
      return;
    }

    const radioisotop = radioisotopSelect.value;
    const material = materialPerisaiSelect.value;

    if (!radioisotop || !material) {
      hvlInfoInput.value = "";
      return;
    }

    try {
      const data = await fetchJSON(
        `/paparan/api/hvl/${encodeURIComponent(radioisotop)}/${encodeURIComponent(material)}`
      );

      if (data.success) {
        hvlInfoInput.value =
          `${data.hvl} ${data.satuan}`;
      } else {
        hvlInfoInput.value = "";
      }

    } catch (error) {
      handleError(error);
      hvlInfoInput.value = "";
    }
  }

  /* =========================
     EVENT KONDISI
  ========================= */
  kondisiInputs.forEach((input) => {
    input.addEventListener("change", togglePerisai);
  });

  /* =========================
     EVENT RADIOISOTOP
  ========================= */
  radioisotopSelect?.addEventListener(
    "change",
    async () => {
      await updateGamma();
      await updateHVL();
    }
  );

  /* =========================
     EVENT MATERIAL
  ========================= */
  materialPerisaiSelect?.addEventListener(
    "change",
    updateHVL
  );

  /* =========================
     LOAD AWAL
  ========================= */
  togglePerisai();
  updateGamma();
  updateHVL();
  validasiAktivitas();
  validasiJarak();
  validasiTebalPerisai();
}