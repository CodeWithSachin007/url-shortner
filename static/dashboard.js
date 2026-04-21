document.addEventListener("DOMContentLoaded", () => {
  const canvas = document.getElementById("analyticsChart");
  if (!canvas) return;

  new Chart(canvas, {
    type: "bar",
    data: {
      labels: chartLabels,
      datasets: [{
        label: "Clicks",
        data: chartData,
        backgroundColor: "rgba(56, 189, 248, 0.8)",
        borderColor: "rgba(14, 165, 233, 1)",
        borderWidth: 1,
        borderRadius: 10
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          labels: { color: "#e5eefc" }
        }
      },
      scales: {
        x: { ticks: { color: "#e5eefc" }, grid: { color: "rgba(255,255,255,0.08)" } },
        y: { ticks: { color: "#e5eefc" }, grid: { color: "rgba(255,255,255,0.08)" }, beginAtZero: true }
      }
    }
  });
});
