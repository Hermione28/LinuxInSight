import psutil
import time

def get_uptime():
    try:
        uptime_seconds = time.time() - psutil.boot_time()
        uptime_hours = uptime_seconds // 3600
        return uptime_hours
    except:
        return 0
