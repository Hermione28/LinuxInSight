import time
from collections import deque

from collectors.cpu import get_cpu
from collectors.memory import get_memory
from collectors.disk import get_disk
from collectors.network import get_network
from collectors.docker import get_containers

# store last 20 values
cpu_history = deque(maxlen=20)
memory_history = deque(maxlen=20)

def get_metrics():
    cpu = get_cpu()
    memory = get_memory()

    cpu_history.append(cpu)
    memory_history.append(memory)

    return {
        "timestamp": time.time(),
        "cpu": cpu,
        "memory": memory,
        "disk": get_disk(),
        "network": get_network(),
        "containers": get_containers(),
        "cpu_history": list(cpu_history),
        "memory_history": list(memory_history)
    }
