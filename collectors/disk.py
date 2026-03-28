
import psutil

def get_disk():
    disk = psutil.disk_usage('/')
    return disk.percent
