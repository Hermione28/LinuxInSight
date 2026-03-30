
import logging
from flask import Flask, jsonify, render_template
from database import init_db, insert_metrics, get_last_metrics
from services.metrics_service import get_all_metrics
from services.health_service import calculate_health
from services.analysis_service import analyze_trend, detect_anomaly
from database import get_last_n_metrics
app = Flask(__name__)

# 🔥 Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# Initialize DB
init_db()


@app.route('/test')
def test():
    logger.info("Test endpoint hit")
    return "Route Working"


@app.route('/login')
def login():
    return render_template('login.html')


# Dashboard UI
@app.route('/')
def index():
    return render_template('index.html')


# 🔥 API: real-time metrics + store in DB
@app.route("/metrics")
def metrics():
    try:
        data = get_all_metrics()

        # ✅ FIXED INDENTATION
        insert_metrics(
            data.get("cpu", 0),
            data.get("memory", 0),
            data.get("disk", 0),
            data.get("network", 0)
        )

        logger.info("Metrics fetched and stored successfully")

        return jsonify(data)

    except Exception as e:
        logger.error(f"Error in /metrics: {str(e)}")
        return jsonify({"error": "Failed to fetch metrics"}), 500


# 🔥 API: history for graphs
@app.route("/history")
def history():
    try:
        data = get_last_metrics()
        logger.info("History data fetched")
        return jsonify(data)

    except Exception as e:
        logger.error(f"Error in /history: {str(e)}")
        return jsonify({"error": "Failed to fetch history"}), 500


# ✅ Health check endpoint
@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == '__main__':
    logger.info("Starting Flask app...")
    app.run(debug=True)
