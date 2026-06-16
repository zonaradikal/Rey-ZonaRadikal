
/* =========================
   RIWAYAT TABS
========================= */
function setupRiwayatTabs() {
  const tabs = document.querySelectorAll(".Riwayat-Tab");
  const panels = document.querySelectorAll(".Riwayat-Panel");

  if (!tabs.length || !panels.length) {
    return;
  }

  function activateRiwayatTab(target, updateUrl = false) {
    const targetTab = document.querySelector(`.Riwayat-Tab[data-tab="${target}"]`);
    const targetPanel = document.querySelector(`.Riwayat-Panel[data-panel="${target}"]`);

    if (!targetTab || !targetPanel) {
      return;
    }

    tabs.forEach((tab) => {
      tab.classList.remove("is-active");
    });

    panels.forEach((panel) => {
      panel.classList.remove("is-active");
    });

    targetTab.classList.add("is-active");
    targetPanel.classList.add("is-active");

    if (updateUrl) {
      const url = new URL(window.location.href);

      url.searchParams.set("tab", target);

      window.history.replaceState({}, "", url);
    }
  }

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      activateRiwayatTab(tab.dataset.tab, true);
    });
  });

  const selectedTab = new URLSearchParams(window.location.search).get("tab");
  if (selectedTab) {
    activateRiwayatTab(selectedTab);
  }
}

/* =========================
   RIWAYAT SEARCH
========================= */
function setupRiwayatSearch() {
  const searchInput = document.getElementById("riwayatSearch");
  const tabButtons = document.querySelectorAll(".Riwayat-Tab");

  if (!searchInput) {
    return;
  }

  function getActivePanel() {
    return document.querySelector(".Riwayat-Panel.is-active");
  }

  function removeEmptySearchRow() {
    document.querySelectorAll(".Riwayat-Empty-Search").forEach((row) => {
      row.remove();
    });
  }

  function filterActiveTable() {
    const keyword = searchInput.value.toLowerCase().trim();
    const panel = getActivePanel();

    if (!panel || !panel._riwayatRows) {
      return;
    }

    const rows = panel._riwayatRows;
    const table = panel.querySelector(".Riwayat-Table");
    const tbody = table.querySelector("tbody");
    const pagination = panel.querySelector(".Riwayat-Pagination");

    removeEmptySearchRow();

    if (!keyword) {
      if (pagination) {
        pagination.style.display = "";
      }

      panel._riwayatCurrentPage = 1;

      panel.dispatchEvent(
        new Event("riwayat-reset-pagination")
      );

      return;
    }

    if (pagination) {
      pagination.style.display = "none";
    }

    let visibleCount = 0;

    rows.forEach((row) => {
      const match = row.textContent.toLowerCase().includes(keyword);

      row.hidden = !match;

      if (match) {
        visibleCount++;
      }
    });

    if (!visibleCount) {
      const columnCount = table.querySelectorAll("thead th").length;

      const emptyRow = document.createElement("tr");
      emptyRow.className = "Riwayat-Empty-Search";

      const emptyCell = document.createElement("td");
      emptyCell.colSpan = columnCount;
      emptyCell.textContent = "Tidak ada data yang sesuai dengan kata kunci pencarian.";

      emptyRow.appendChild(emptyCell);
      tbody.appendChild(emptyRow);
    }
  }

  searchInput.addEventListener(
    "input",
    debounce(filterActiveTable)
  );

  tabButtons.forEach((button) => {
    button.addEventListener("click", () => {
      setTimeout(filterActiveTable, 0);
    });
  });
}

/* =========================
   RIWAYAT PAGINATION
========================= */
function setupRiwayatPagination() {
  const ROWS_PER_PAGE = 10;
  const MAX_VISIBLE_PAGES = 5;

  const panels = document.querySelectorAll(".Riwayat-Panel");

  panels.forEach((panel) => {
    const table = panel.querySelector(".Riwayat-Table");

    if (!table) {
      return;
    }

    const tbody = table.querySelector("tbody");

    if (!tbody) {
      return;
    }

    const rows = Array.from(
      tbody.querySelectorAll("tr")
    );

    panel._riwayatRows = rows;
    panel._riwayatCurrentPage = 1;

    if (rows.length <= ROWS_PER_PAGE) {
      return;
    }

    const totalPages = Math.ceil(
      rows.length / ROWS_PER_PAGE
    );

    const pagination = document.createElement("div");
    pagination.className = "Riwayat-Pagination";

    function renderPagination() {
      pagination.innerHTML = "";

      const prevButton = document.createElement("button");

      prevButton.type = "button";
      prevButton.className = "Riwayat-Page Riwayat-Page-Nav";
      prevButton.textContent = "←";
      prevButton.disabled = panel._riwayatCurrentPage === 1;

      prevButton.addEventListener("click", () => {
        if (panel._riwayatCurrentPage > 1) {
          panel._riwayatCurrentPage--;
          renderRows();
        }
      });

      pagination.appendChild(prevButton);

      let startPage = Math.max(
        1,
        panel._riwayatCurrentPage -
        Math.floor(MAX_VISIBLE_PAGES / 2)
      );

      let endPage = startPage + MAX_VISIBLE_PAGES - 1;

      if (endPage > totalPages) {
        endPage = totalPages;

        startPage = Math.max(
          1,
          endPage - MAX_VISIBLE_PAGES + 1
        );
      }

      for (let page = startPage; page <= endPage; page++) {
        const button = document.createElement("button");

        button.type = "button";
        button.className = "Riwayat-Page";
        button.textContent = page;

        if (page === panel._riwayatCurrentPage) {
          button.classList.add("is-active");
        }

        button.addEventListener("click", () => {
          panel._riwayatCurrentPage = page;
          renderRows();
        });

        pagination.appendChild(button);
      }

      const nextButton = document.createElement("button");

      nextButton.type = "button";
      nextButton.className = "Riwayat-Page Riwayat-Page-Nav";
      nextButton.textContent = "→";
      nextButton.disabled = panel._riwayatCurrentPage === totalPages;

      nextButton.addEventListener("click", () => {
        if (panel._riwayatCurrentPage < totalPages) {
          panel._riwayatCurrentPage++;
          renderRows();
        }
      });

      pagination.appendChild(nextButton);
    }

    function renderRows() {
      const start =
        (panel._riwayatCurrentPage - 1) *
        ROWS_PER_PAGE;

      const end = start + ROWS_PER_PAGE;

      rows.forEach((row, index) => {
        row.hidden = !(index >= start && index < end);
      });

      renderPagination();
    }

    panel.addEventListener(
      "riwayat-reset-pagination",
      renderRows
    );

    rows.forEach((row) => {
      row.hidden = true;
    });

    panel.appendChild(pagination);

    renderRows();
  });
}