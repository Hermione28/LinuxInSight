import psutil
import time

def get_top_processes(limit=5):
    processes = []

    # 🔥 first call to initialize cpu %
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent(interval=None)
        except:
            pass

    time.sleep(0.5)  # give time to calculate

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append({
                "pid": proc.info['pid'],
                "name": proc.info['name'],
                "cpu": proc.info['cpu_percent'],
                "memory": round(proc.info['memory_percent'], 2)
            })
        except:
            continue

    processes = sorted(processes, key=lambda x: x['cpu'], reverse=True)
    return processes[:limit]
