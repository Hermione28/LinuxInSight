try:
    import docker
    client = docker.from_env()
except Exception:
    client = None


def get_docker_metrics():
    if client is None:
        return []

    try:
        containers = client.containers.list()
        container_data = []

        for container in containers:
            try:
                stats = container.stats(stream=False)

                # CPU calculation
                cpu_delta = stats["cpu_stats"]["cpu_usage"]["total_usage"] - \
                            stats["precpu_stats"]["cpu_usage"]["total_usage"]

                system_delta = stats["cpu_stats"]["system_cpu_usage"] - \
                            stats["precpu_stats"]["system_cpu_usage"]

                cpu_percent = 0.0
                if system_delta > 0.0 and cpu_delta > 0.0:
                    cpu_count = len(stats["cpu_stats"]["cpu_usage"].get("percpu_usage", [])) or 1
                    cpu_percent = (cpu_delta / system_delta) * cpu_count * 100.0

                # Memory calculation
                memory_usage = stats["memory_stats"]["usage"]
                cache = stats["memory_stats"].get("stats", {}).get("cache", 0)
                memory_usage -= cache

                memory_limit = stats["memory_stats"]["limit"]
                memory_percent = (memory_usage / memory_limit) * 100.0 if memory_limit > 0 else 0

                container_data.append({
                    "name": container.name,
                    "status": container.status,  # ✅ FIX (IMPORTANT)
                    "cpu": round(cpu_percent, 2),
                    "memory": round(memory_percent, 2),
                    "memory_mb": round(memory_usage / (1024 * 1024), 2)
                })

            except Exception as e:
                container_data.append({
                    "name": container.name,
                    "status": "error",
                    "cpu": 0,
                    "memory": 0,
                    "memory_mb": 0
                })

        return container_data

    except Exception:
        return []
