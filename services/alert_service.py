def check_alerts(metrics):
    alerts = []

    if metrics["cpu"] > 80:
        alerts.append("High CPU Usage!")

    if metrics["memory"] > 80:
        alerts.append("High Memory Usage!")

    return alerts
