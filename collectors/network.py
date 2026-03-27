import psutil

def get_network():
    net = psutil.net_io_counters()
    return {
        "sent": net.bytes_sent,
        "recv": net.bytes_recv
    }
