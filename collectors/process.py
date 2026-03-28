import psutil

def get_top_processes(limit=5):
    processes = []

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
