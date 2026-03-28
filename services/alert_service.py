def generate_alerts(data):
    alerts = []

    cpu = data.get("cpu", 0)
    memory = data.get("memory", 0)
    disk = data.get("disk", 0)

    # 🚨 CPU Alert
    if cpu > 80:
        alerts.append({
            "type": "CPU",
            "message": f"High CPU usage: {cpu}%"
        })

    # 🚨 Memory Alert
    if memory > 80:
        alerts.append({
            "type": "Memory",
            "message": f"High Memory usage: {memory}%"
        })

    # 🚨 Disk Alert
    if disk > 85:
        alerts.append({
            "type": "Disk",
            "message": f"High Disk usage: {disk}%"
        })

    return alerts
