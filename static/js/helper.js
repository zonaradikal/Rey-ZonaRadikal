
/* =========================
   HELPER
========================= */
function setupHelperButton() {
  const wrapper = document.querySelector(".Helper-Wrapper");
  const button = document.getElementById("Helper-Button");
  const overlay = document.getElementById("Helper-Overlay");
  const closeButton = document.getElementById("Helper-Close");
  const content = document.getElementById("Helper-Content");

  if (!wrapper || !button || !overlay || !closeButton || !content) {
    return;
  }

  const halaman = wrapper.dataset.helperPage;

  if (!halaman) {
    return;
  }

  let hasLoaded = false;

  button.addEventListener("click", async () => {
    openHelperOverlay(overlay, closeButton);

    if (!hasLoaded) {
      await loadHelperContent(halaman, content);
      hasLoaded = true;
    }
  });

  closeButton.addEventListener("click", () => {
    closeHelperOverlay(overlay);
  });

  overlay.addEventListener("click", (event) => {
    if (event.target === overlay) {
      closeHelperOverlay(overlay);
    }
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && overlay.classList.contains("active")) {
      closeHelperOverlay(overlay);
    }
  });
}

/* =========================
   OVERLAY
========================= */
function openHelperOverlay(overlay, focusTarget = null) {
  overlay.classList.add("active");
  overlay.setAttribute("aria-hidden", "false");
  document.body.style.overflow = "hidden";

  if (focusTarget) {
    focusTarget.focus();
  }
}

function closeHelperOverlay(overlay) {
  overlay.classList.remove("active");
  overlay.setAttribute("aria-hidden", "true");
  document.body.style.overflow = "";
}

/* =========================
   LOAD CONTENT
========================= */
async function loadHelperContent(halaman, content) {
  content.innerHTML = `
    <p class="Helper-Empty">
      Memuat bantuan...
    </p>
  `;

  try {
    showLoading();

    const data = await fetchJSON(`/bantuan/${halaman}`);

    if (!Array.isArray(data) || !data.length) {
      content.innerHTML = `
        <p class="Helper-Empty">
          Belum ada bantuan untuk halaman ini.
        </p>
      `;
      return;
    }

    content.innerHTML = data.map((item) => `
      <article class="Helper-Item">
        <h3 class="Helper-Item-Title">
          ${item.urutan}. ${escapeHTML(item.judul)}
        </h3>

        <p class="Helper-Item-Text">
          ${escapeHTML(item.isi)}
        </p>
      </article>
    `).join("");

  } catch (error) {

    handleError(error);

    content.innerHTML = `
      <p class="Helper-Empty">
        Bantuan gagal dimuat. Silakan coba lagi.
      </p>
    `;

  } finally {

    hideLoading();

  }
}