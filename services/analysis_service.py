import numpy as np

def analyze_trend(history):
    if len(history) < 2:
        return "➡️ Stable"

    try:
        if history[-1] > history[-2]:
            return "📈 Increasing"
        elif history[-1] < history[-2]:
            return "📉 Decreasing"
        return "➡️ Stable"
    except:
        return "➡️ Stable"


# 🔥 AI-based anomaly detection (Z-score method)
def detect_anomaly(value, history=None):
    try:
        if history is None or len(history) < 5:
            return False

        mean = np.mean(history)
        std = np.std(history)

        if std == 0:
            return False

        z_score = (value - mean) / std

        return bool(abs(z_score) > 2)   # ✅ FIXED

    except:
        return False
