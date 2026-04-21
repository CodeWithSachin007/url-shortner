document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".loading-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      btn.classList.add("loading");
      btn.dataset.originalText = btn.textContent;
      setTimeout(() => {
        if (btn.dataset.originalText) btn.textContent = btn.dataset.originalText;
        btn.classList.remove("loading");
      }, 1200);
    });
  });

  document.querySelectorAll(".copy-btn").forEach((btn) => {
    btn.addEventListener("click", async () => {
      const targetId = btn.getAttribute("data-copy-target");
      const input = document.getElementById(targetId);
      if (!input) return;
      try {
        await navigator.clipboard.writeText(input.value);
        alert("Short URL copied successfully!");
      } catch (error) {
        alert("Copy failed. Please copy manually.");
      }
    });
  });
});
