def calculate_health(metrics):
    cpu = metrics.get("cpu", 0)
    memory = metrics.get("memory", 0)
    disk = metrics.get("disk", 0)

    score = 100

    # Reduce score based on usage
    if cpu > 80:
        score -= 30
    elif cpu > 60:
        score -= 15

    if memory > 80:
        score -= 30
    elif memory > 60:
        score -= 15

    if disk > 80:
        score -= 20

    return max(score, 0)
