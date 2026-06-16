
/* =========================
   CONFIG
========================= */
const CONFIG = {
  searchDelay: 300,
  inputInfoDelay: 1500
};

/* =========================
   UTILITIES
========================= */
const $ = (selector, parent = document) => parent.querySelector(selector);
const $$ = (selector, parent = document) => parent.querySelectorAll(selector);

function debounce(callback, delay = CONFIG.searchDelay) {
  let timeout;

  return (...args) => {
    clearTimeout(timeout);
    timeout = setTimeout(() => callback(...args), delay);
  };
}

function escapeHTML(text) {
  return String(text)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

/* =========================
   TOAST
========================= */
function showToast(message, type = "info") {
  let container = document.getElementById("Global-Toast");

  if (!container) {
    container = document.createElement("div");
    container.id = "Global-Toast";
    container.className = "Global-Toast";
    document.body.appendChild(container);
  }

  const toast = document.createElement("div");

  toast.className = `Toast Toast-${type}`;
  toast.textContent = message;

  container.appendChild(toast);
  setTimeout(() => {
    toast.remove();
  }, 4000);
}

/* =========================
   LOADING OVERLAY
========================= */
function showLoading() {
  let overlay = document.getElementById("Global-Loading");

  if (!overlay) {
    overlay = document.createElement("div");

    overlay.id = "Global-Loading";
    overlay.className = "Global-Loading";

    overlay.innerHTML = `
      <div class="Global-Loading-Box">
        Memuat...
      </div>
    `;

    document.body.appendChild(overlay);
  }

  overlay.classList.add("active");
}

function hideLoading() {
  const overlay = document.getElementById("Global-Loading");

  if (!overlay) {
    return;
  }

  overlay.classList.remove("active");
}

/* =========================
   API UTILITIES
========================= */
async function fetchJSON(url) {
  const response = await fetch(url);

  if (!response.ok) {
    throw new Error("Request gagal");
  }

  return response.json();
}

function handleError(error) {
  console.error(error);
  showToast("Terjadi kesalahan sistem.", "error");
}

/* =========================
   NAVBAR MOBILE
========================= */
function setupMobileNavbar() {
  const navBar = $(".Nav-Bar");
  const navList = $(".Nav-List");
  const openMenu = $(".Nav-Open");
  const closeMenu = $(".Nav-Close");
  const navLinks = $$(".Nav-List a");

  if (!navBar || !navList || !openMenu || !closeMenu) {
    return;
  }

  function openMobileMenu() {
    navBar.classList.add("active");
    navList.classList.add("active");
  }

  function closeMobileMenu() {
    navBar.classList.remove("active");
    navList.classList.remove("active");
  }

  openMenu.addEventListener("click", openMobileMenu);
  closeMenu.addEventListener("click", closeMobileMenu);

  navLinks.forEach((link) => {
    link.addEventListener("click", closeMobileMenu);
  });
}

/* =========================
   INPUT INFO
========================= */
function setupInputInfo() {
  const fields = $$(".Input-Field");

  fields.forEach((field) => {
    const info = $(".Input-Info", field);

    if (!info) {
      return;
    }

    let timer;

    const showInfo = () => {
      timer = setTimeout(() => {
        info.classList.add("active");
      }, CONFIG.inputInfoDelay);
    };

    const hideInfo = () => {
      clearTimeout(timer);
      info.classList.remove("active");
    };

    field.addEventListener("mouseenter", showInfo);
    field.addEventListener("mouseleave", hideInfo);

    const input = field.querySelector("input, select, textarea");

    if (input) {
      input.addEventListener("focus", showInfo);
      input.addEventListener("blur", hideInfo);
    }
  });
}

/* =========================
   CALCULATION LOADING
========================= */
function setupCalculationLoading() {
  const forms = $$("form");

  forms.forEach((form) => {
    const action = $(".Cal-Action", form);
    const submitButton = $(".Button-Primary", form);

    if (!action || !submitButton) {
      return;
    }

    form.addEventListener("submit", () => {
      submitButton.disabled = true;
      submitButton.dataset.originalText = submitButton.textContent;
      submitButton.textContent = "Menghitung...";
      submitButton.classList.add("loading");
    });
  });
}

/* =========================
   BERANDA ACCORDION
========================= */
function setupBerandaAccordion() {
  const sections = $$(".Beranda-Section");

  if (!sections.length) {
    return;
  }

  sections.forEach((section) => {
    const trigger = $(".Beranda-Trigger", section);
    const content = $(".Beranda-Content", section);

    if (!trigger || !content) {
      return;
    }

    trigger.addEventListener("click", () => {
      const isActive = section.classList.contains("is-active");

      sections.forEach((item) => {
        item.classList.remove("is-active");
      });

      if (!isActive) {
        section.classList.add("is-active");
      }
    });
  });
}

/* =========================
   PANDUAN TABS
========================= */
function setupPanduanTabs() {
  const tabs = $$(".Panduan-Tab");
  const panels = $$(".Panduan-Panel");

  if (!tabs.length || !panels.length) {
    return;
  }

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      const target = tab.dataset.tab;

      tabs.forEach((item) => {
        item.classList.remove("is-active");
      });

      panels.forEach((panel) => {
        panel.classList.remove("is-active");
      });

      tab.classList.add("is-active");

      const activePanel = document.querySelector(`.Panduan-Panel[data-panel="${target}"]`);
      if (activePanel) {
        activePanel.classList.add("is-active");
      }
    });
  });
}

/* =========================
   PANDUAN ACCORDION
========================= */
function setupPanduanAccordion() {
  const accordions = $$(".Accordion-Section");

  accordions.forEach((section) => {
    const trigger = $(".Accordion-Trigger", section);

    if (!trigger) {
      return;
    }

    trigger.addEventListener("click", () => {
      section.classList.toggle("active");
    });
  });
}