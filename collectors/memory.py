import psutil

def get_memory():
    mem = psutil.virtual_memory()
    return mem.percent
