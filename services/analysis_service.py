def analyze_trend(history):
    if len(history) < 2:
        return "stable"

    if history[-1] > history[-2]:
        return "increasing"
    elif history[-1] < history[-2]:
        return "decreasing"
    return "stable"


def detect_anomaly(value, threshold=85):
    return value > threshold
