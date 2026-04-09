## LinuxInSight – System Monitoring Dashboard

This project is a real-time system monitoring dashboard built using **Flask (Python)** that provides insights into system performance such as CPU, memory, disk, network usage, Docker container stats, and anomaly detection.

---

## Preview

![Dashboard Screenshot 1](ASSETS/Dashboard1.png)
![Dashboard Screenshot 2](ASSETS/Dashboard2.png)

---

### Requirements

To run this project, you will need the following dependencies:

* Python 3.7 or higher
* Flask
* psutil
* Docker SDK for Python
* SQLite (comes pre-installed with Python)

---

### Installation

1. Install Python 3.7 or higher on your system.

2. Clone the repository:

```
git clone https://github.com/your-username/LinuxInSight.git
cd LinuxInSight
```

3. Install required dependencies:

```
pip install -r requirements.txt
```

4. (Optional) Run using Docker:

```
docker-compose up --build
```

---

### Usage

1. Run the Flask application:

```
python app.py
```

2. Open your browser and go to:

```
http://127.0.0.1:5000/
```

3. The dashboard will display real-time system metrics.

---

### How it works

The system is divided into multiple layers:

* **Collectors Layer**
  Uses `psutil` and Docker APIs to fetch system-level metrics such as CPU, memory, disk, and network usage.

* **Service Layer**
  Processes collected data to:

  * Calculate system health score
  * Detect anomalies
  * Analyze usage trends

* **Database Layer**
  Stores historical metrics in SQLite for trend analysis.

* **Frontend Dashboard**
  Displays real-time metrics, graphs, and system insights using JavaScript and charts.

---

### Features

* Real-time CPU, Memory, Disk, Network monitoring
* Docker container monitoring
* System health score calculation
* Trend analysis (increasing/decreasing usage)
* Anomaly detection
* Top processes tracking
* Interactive dashboard UI

---

## File Descriptions

* `app.py`: Main Flask application
* `database.py`: Handles database operations
* `collectors/`: Contains system metric collectors (CPU, memory, disk, network, Docker, etc.)
* `services/`: Business logic (health, alerts, analysis, scheduler)
* `templates/index.html`: Dashboard UI
* `static/js/`: Frontend scripts for charts and updates
* `metrics.db`: SQLite database storing metrics
* `docker-compose.yml`: Docker configuration

---

### Examples

![Example Dashboard 1](ASSETS/Dashboard1.png)
![Example Dashboard 2](ASSETS/Dashboard2.png)

---

### Future Improvements

* Add alert notifications (Email/Slack)
* Improve anomaly detection using ML models
* Multi-system monitoring support
* Authentication and user roles
* Advanced visualizations

---
