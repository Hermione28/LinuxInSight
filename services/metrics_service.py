import logging

from collectors.cpu import get_cpu_usage
from collectors.memory import get_memory_usage
from collectors.disk import get_disk_usage
from collectors.network import get_network_usage
from collectors.process import get_top_processes
from collectors.docker import get_docker_metrics
from collectors.system import get_uptime

from services.alert_service import check_alerts

logger = logging.getLogger(__name__)


def get_all_metrics():
    try:
        data = {
            "cpu": get_cpu_usage(),
            "memory": get_memory_usage(),
            "disk": get_disk_usage(),
            "network": get_network_usage(),
            "docker": get_docker_metrics(),
            "processes": get_top_processes(),
            "uptime": get_uptime()
        }

        # 🔥 Alerts
        data["alerts"] = check_alerts(data)

        logger.info("Metrics collected successfully")

        return data

    except Exception as e:
        logger.error(f"Metrics Error: {str(e)}")

        # safe fallback response
        return {
            "cpu": 0,
            "memory": 0,
            "disk": 0,
            "network": 0,
            "docker": [],
            "processes": [],
            "uptime": "N/A",
            "alerts": ["Error fetching metrics"]
        }
