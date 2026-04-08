window.onload = function () {
  const cpuEl = document.getElementById("cpu");
  const memoryEl = document.getElementById("memory");
  const diskEl = document.getElementById("disk");
  const networkEl = document.getElementById("network");

  const healthEl = document.getElementById("health");
  const cpuTrendEl = document.getElementById("cpu_trend");
  const memoryTrendEl = document.getElementById("memory_trend");
  const cpuAnomalyEl = document.getElementById("cpu_anomaly");
  const memoryAnomalyEl = document.getElementById("memory_anomaly");
  const dockerEl = document.getElementById("docker");

  const processTable = document.getElementById("processTable");

  function createChart(id, label, color) {
    const ctx = document.getElementById(id).getContext("2d");

    return new Chart(ctx, {
      type: "line",
      data: {
        labels: [],
        datasets: [
          {
            label: label,
            data: [],
            borderColor: color,
            backgroundColor: color + "33",
            borderWidth: 2,
            tension: 0.4,
            fill: true,
          },
        ],
      },
      options: {
        animation: false,
        plugins: { legend: { display: false } },
        scales: {
          x: { ticks: { color: "#9ca3af", maxTicksLimit: 6 } },
          y: { ticks: { color: "#9ca3af" }, beginAtZero: true },
        },
      },
    });
  }

  const cpuChart = createChart("cpuChart", "CPU", "#ef4444");
  const memoryChart = createChart("memoryChart", "Memory", "#3b82f6");
  const diskChart = createChart("diskChart", "Disk", "#f59e0b");
  const networkChart = createChart("networkChart", "Network", "#10b981");

  // 🔥 helper for badge UI
  function badge(text, color) {
    return `<span style="
      padding:4px 8px;
      border-radius:6px;
      font-size:12px;
      font-weight:500;
      background:${color}22;
      color:${color};
    ">${text}</span>`;
  }

  // 🔥 FETCH METRICS
  async function fetchMetrics() {
    const res = await fetch("/metrics");
    const data = await res.json();

    // ✅ cards
    cpuEl.innerText = data.cpu + "%";
    memoryEl.innerText = data.memory + "%";
    diskEl.innerText = data.disk + "%";
    networkEl.innerText = data.network;

    let color = "#10b981"; // green

    if (data.health < 50)
      color = "#ef4444"; // red
    else if (data.health < 75) color = "#f59e0b"; // yellow

    healthEl.innerHTML = `
  <span style="
    font-size:28px;
    font-weight:bold;
    color:${color}
  ">
    ${data.health}
  </span>
`;

    // ✅ trend
    cpuTrendEl.innerText = data.cpu_trend;
    memoryTrendEl.innerText = data.memory_trend;

    // ✅ anomaly (🔥 upgraded UI)
    cpuAnomalyEl.innerHTML = data.cpu_anomaly
      ? badge("⚠️ Anomaly", "#ef4444")
      : badge("Normal", "#10b981");

    memoryAnomalyEl.innerHTML = data.memory_anomaly
      ? badge("⚠️ Anomaly", "#ef4444")
      : badge("Normal", "#10b981");

    // ✅ Docker UI (🔥 improved)
    dockerEl.innerHTML = "";

    if (data.docker && data.docker.length > 0) {
      data.docker.forEach((c) => {
        dockerEl.innerHTML += `
      <div style="
        background:#1f2937;
        padding:10px;
        margin:6px 0;
        border-radius:8px;
        font-size:14px">

        <strong>${c.name}</strong>

        <div style="margin-top:5px">
          Status: 
          <span style="color:${c.status === "running" ? "#10b981" : "#ef4444"}">
            ${c.status}
          </span>
        </div>

        <div>CPU: ${c.cpu}%</div>
        <div>Memory: ${c.memory}% (${c.memory_mb} MB)</div>
      </div>
    `;
      });
    } else {
      dockerEl.innerHTML = "<p>No containers running</p>";
    }

    // ✅ process table
    processTable.innerHTML = "";
    data.processes.forEach((p) => {
      processTable.innerHTML += `
        <tr>
          <td>${p.pid}</td>
          <td>${p.name}</td>
          <td>${p.cpu}</td>
          <td>${p.memory}</td>
        </tr>
      `;
    });
  }

  // 🔥 HISTORY (GRAPHS)
  async function loadHistory() {
    const res = await fetch("/history");
    const history = await res.json();

    const labels = history.map((h) =>
      new Date(h.timestamp).toLocaleTimeString(),
    );

    cpuChart.data.labels = labels;
    memoryChart.data.labels = labels;
    diskChart.data.labels = labels;
    networkChart.data.labels = labels;

    cpuChart.data.datasets[0].data = history.map((h) => h.cpu);
    memoryChart.data.datasets[0].data = history.map((h) => h.memory);
    diskChart.data.datasets[0].data = history.map((h) => h.disk);
    networkChart.data.datasets[0].data = history.map((h) => h.network);

    cpuChart.update();
    memoryChart.update();
    diskChart.update();
    networkChart.update();
  }

  // 🚀 RUN
  fetchMetrics();
  loadHistory();

  setInterval(fetchMetrics, 3000);
  setInterval(loadHistory, 10000);
};
