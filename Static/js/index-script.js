window.onload = function () {
  const cpuEl = document.getElementById("cpu");
  const memoryEl = document.getElementById("memory");
  const diskEl = document.getElementById("disk");
  const networkEl = document.getElementById("network");
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
        plugins: {
          legend: { display: false },
        },
        scales: {
          x: {
            ticks: { color: "#9ca3af", maxTicksLimit: 5 },
          },
          y: {
            ticks: { color: "#9ca3af" },
            beginAtZero: true,
          },
        },
      },
    });
  }

  const cpuChart = createChart("cpuChart", "CPU", "#ef4444");
  const memoryChart = createChart("memoryChart", "Memory", "#3b82f6");
  const diskChart = createChart("diskChart", "Disk", "#f59e0b");
  const networkChart = createChart("networkChart", "Network", "#10b981");

  function update(chart, value) {
    const time = new Date().toLocaleTimeString();

    chart.data.labels.push(time);
    chart.data.datasets[0].data.push(value);

    if (chart.data.labels.length > 8) {
      chart.data.labels.shift();
      chart.data.datasets[0].data.shift();
    }

    chart.update();
  }

  async function fetchMetrics() {
    const res = await fetch("/metrics");
    const data = await res.json();

    cpuEl.innerText = data.cpu + "%";
    memoryEl.innerText = data.memory + "%";
    diskEl.innerText = data.disk + "%";
    networkEl.innerText = data.network;

    update(cpuChart, data.cpu);
    update(memoryChart, data.memory);
    update(diskChart, data.disk);
    update(networkChart, data.network);

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

  setInterval(fetchMetrics, 3000);
  fetchMetrics();
};
