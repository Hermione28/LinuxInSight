from collectors.cpu import get_cpu_usage
from collectors.memory import get_memory_usage
from collectors.disk import get_disk_usage
from collectors.network import get_network_usage
from collectors.docker import get_docker_containers
from collectors.process import get_top_processes

from services.alert_service import generate_alerts
from database import insert_metrics


def collect_all_metrics():
    try:
        data = {
            "cpu": get_cpu_usage(),
            "memory": get_memory_usage(),
            "disk": get_disk_usage(),
            "network": get_network_usage(),
            "docker": get_docker_containers(),
            "processes": get_top_processes()
        }

        # Alerts
        data["alerts"] = generate_alerts(data)

        # Store in DB (safe)
        try:
            insert_metrics(data)
        except Exception as e:
            print("DB Error:", e)

        return data

    except Exception as e:
        print("Metrics Error:", e)
        return {
            "cpu": 0,
            "memory": 0,
            "disk": 0,
            "network": 0,
            "docker": [],
            "processes": [],
            "alerts": []
        }
