document.addEventListener("DOMContentLoaded", () => {
  const form = document.querySelector(".auth-form");
  const inputs = document.querySelectorAll(".auth-form input");

  inputs.forEach((input) => {
    const formInput = input.closest(".form-input");
    const info = formInput?.querySelector(".input-info");

    input.addEventListener("focus", () => {
      if (info && input.dataset.info) {
        info.textContent = input.dataset.info;
      }
    });

    input.addEventListener("blur", () => {
      if (info) info.textContent = "";
    });
  });


  /* === SHOW HIDE PASSWORD === */
  document.querySelectorAll(".toggle-password").forEach((button) => {
    button.addEventListener("click", () => {
      const input = button.closest(".form-input")?.querySelector("input");

      if (!input) return;

      const show = input.type === "password";
      input.type = show ? "text" : "password";

      const icon = button.querySelector("i");
      icon?.classList.toggle("fa-eye");
      icon?.classList.toggle("fa-eye-slash");
    });
  });

  
  /* === LOADING SUBMIT === */
  form?.addEventListener("submit", () => {
    if (!form.checkValidity()) return;

    const button = form.querySelector(".auth-button");

    if (!button) return;

    button.disabled = true;
    button.classList.add("loading");
    button.textContent = "Memproses...";
  });
});  