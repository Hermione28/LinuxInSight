import logging
from flask import Flask, jsonify, render_template
from database import init_db, insert_metrics, get_last_metrics, get_last_n_metrics
from services.metrics_service import get_all_metrics
from services.health_service import calculate_health
from services.analysis_service import analyze_trend, detect_anomaly

app = Flask(__name__)

# 🔥 Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# Initialize DB
init_db()


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/metrics")
def metrics():
    try:
        data = get_all_metrics()

        history = get_last_n_metrics(10) or []

        cpu_history = [row[0] for row in history] if history else []
        memory_history = [row[1] for row in history] if history else []

        health_score = calculate_health(data)

        cpu_trend = analyze_trend(cpu_history)
        memory_trend = analyze_trend(memory_history)

        # 🔥 pass history for AI detection
        cpu_anomaly = detect_anomaly(data.get("cpu", 0), cpu_history)
        memory_anomaly = detect_anomaly(data.get("memory", 0), memory_history)

        return jsonify({
            **data,
            "health": health_score,
            "cpu_trend": cpu_trend,
            "memory_trend": memory_trend,
            "cpu_anomaly": cpu_anomaly,
            "memory_anomaly": memory_anomaly
        })

    except Exception as e:
        logger.error(f"ERROR in /metrics: {str(e)}")
        return jsonify({
            "cpu": 0,
            "memory": 0,
            "disk": 0,
            "network": 0,
            "processes": [],
            "docker": [],
            "health": 0,
            "cpu_trend": "error",
            "memory_trend": "error",
            "cpu_anomaly": False,
            "memory_anomaly": False
        })

@app.route("/history")
def history():
    try:
        data = get_last_metrics()
        logger.info("History data fetched")
        return jsonify(data)
    except Exception as e:
        logger.error(f"Error in /history: {str(e)}")
        return jsonify([])


if __name__ == '__main__':
    logger.info("Starting Flask app...")
    app.run(debug=True)
