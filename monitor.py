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

#You will add settings here in Parts 5, 7, and 8. 

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




