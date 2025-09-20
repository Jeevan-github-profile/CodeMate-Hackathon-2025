import os

def cpu_usage():
    # Basic CPU load from /proc/stat (Linux-like)
    try:
        with open("/proc/loadavg") as f:
            return f"CPU Load (1, 5, 15 min): {f.read().strip()}"
    except:
        return "CPU usage info not available"

def memory_usage():
    try:
        with open("/proc/meminfo") as f:
            lines = f.readlines()
            mem_total = lines[0].split()[1]
            mem_free = lines[1].split()[1]
            return f"Memory: Total {mem_total} KB, Free {mem_free} KB"
    except:
        return "Memory info not available"

def processes():
    try:
        return "Running processes: " + ", ".join(os.listdir("/proc"))[:100]
    except:
        return "Process info not available"
