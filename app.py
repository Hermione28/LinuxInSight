from flask import Flask, render_template, jsonify
from services.metrics_service import collect_all_metrics
from database import init_db

app = Flask(__name__)

@app.route('/test')
def test():
    return "Route Working"

@app.route('/login')
def login():
    return render_template('login.html')

# Dashboard UI
@app.route('/')
def index():
    return render_template('index.html')


# API endpoint for metrics
@app.route('/metrics')
def get_metrics():
    data = collect_all_metrics()
    return jsonify(data)


# Optional: Health check endpoint (GOOD PRACTICE)
@app.route('/health')
def health():
    return jsonify({"status": "ok"})


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
