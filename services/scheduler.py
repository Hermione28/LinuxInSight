from collectors import cpu, disk, memory, network
from services.metrics_service import get_all_metrics
from database import insert_metrics
from services.alert_service import check_alerts
import time

def start_scheduler():
    while True:
        data = get_all_metrics()   

        insert_metrics(
    data["cpu"],
    data["memory"],
    data["disk"],
    data["network"]
)

        alerts = check_alerts(data) 
        if alerts:
            print("ALERT:", alerts)

        print("Metrics stored in DB")

        time.sleep(5)
