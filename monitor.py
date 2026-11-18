"""
monitor.py

System information, resource monitoring, warnings, live monitor, and process information for the TB System Resource Monitor.
"""

from logging import info
import os
import platform
import socket
import time

import psutil

#-------------------------------------------------------------------------
#Settings (constants)
#-------------------------------------------------------------------------

# 1 GB = 1024 * 1024 * 1024 bytes
# TODO: Fill in the exponent so this equals the number of bytes in 1 GB.
BYTES_PER_GB = 1024 ** 3

#-------------------------------------------------------------------------
# Part 4: System information
#-------------------------------------------------------------------------

def get_system_info():
    """
    Return a dictionary of basic information about this computer.
    """

    info = {
        "os_name": platform.system(),
        "os_release": platform.release(),
        "hostname": socket.gethostname(),
        "processor": platform.processor(),
        "python_version": platform.python_version(),
    }

    if info["processor"] == "":
        info["processor"] = "Not available"

    return info

def display_system_info():
    """
    Print the system information in a readable manner.
    """

    info = get_system_info()
    
    print()
    print("System Information")
    print("-"*30)

    print(f"Operating System: {info['os_name']}{info['os_name']}")
    print(f"Computer Name: {info['hostname']}")
    print(f"Processor: {info['processor']}")
    print(f"Python Version: {info['python_version']}")

# -------------------------------------------------------------------
# Part 5: CPU, memory, and disk
# -------------------------------------------------------------------

def bytes_to_gb(num_bytes):
    """
    Convert a number of bytes to gigabytes, rounded to 2 decimal places.
    """

    gigabytes = num_bytes / BYTES_PER_GB

    return round(gigabytes, 2)

def get_cpu_usage():
    """
    Return the current CPU usage percentage.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    
    return cpu_usage

def get_memory_usage():
    """
    Return a dictionary with memory (RAM) percent, used GB
    """
    memory = psutil.virtual_memory()

    memory_info = {
        "percent": memory.percent,
        "used_gb": bytes_to_gb(memory.used),
        "total_gb": bytes_to_gb(memory.total),
    }

    return memory_info

def get_disk_path():
    """
    Return the path of the main disk for this operating system.
    """
    system_name = platform.system()
    if system_name == "Windows":
        return "C:\\"
    elif system_name == "Darwin" and os.path.exists("/System/Volumes/Data"):
        return "/System/Volumes/Data"
    else:
        return "/"

def get_disk_usage():
    """
    Return a dictionary with disk percent, used GB, and total GB.
    """
    disk = psutil.disk_usage(get_disk_path())
    disk_info = {
        "percent": disk.percent,
        "used_gb": bytes_to_gb(disk.used),
        "total_gb": bytes_to_gb(disk.total),
    }
    return disk_info



