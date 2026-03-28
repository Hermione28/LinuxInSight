import psutil

def get_network_usage():
    net = psutil.net_io_counters()
    return net.bytes_sent + net.bytes_recv
