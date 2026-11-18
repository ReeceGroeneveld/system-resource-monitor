"""
logger.py

Save resource snapshots to a CSV file for the TB System Resource Monitor.
"""

import csv
import os
from datetime import datetime
from pickle import TRUE

PROJECT_FOLDER = os.path.dirname(os.path.abspath(__file__))

LOGS_FOLDER = os.path.join(PROJECT_FOLDER, "logs")

LOG_FILE = os.path.join(LOGS_FOLDER, "snapshots.csv")

FIELDNAMES = ["timestamp", "cpu_percent", "memory_percent", "disk_percent"]

def get_timestamp():
    """
    Return the current date and time as text, like "2026-10-27 18:30:00".
    """
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def needs_header():
    """
    Return True if the CSV file still needs a header row.
    """
    if not os.path.exists(LOG_FILE):
        return True
    if os.path.getsize(LOG_FILE) == 0:
        return True
    return False

def save_snapshot(summary):
    """
    Add one row to logs/snapshots.csv using a resource summary dictionary.
    Return the path of the file was written.
    """

    os.makedirs(LOGS_FOLDER, exist_ok=True)

    write_header = needs_header()

    row = {
        "timestamp": get_timestamp(),
        "cpu_percent": summary["cpu_percent"],
        "memory_percent": summary["memory_percent"],
        "disk_percent": summary["disk_percent"],
    }

    with open(LOG_FILE, "a", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        if write_header:
            writer.writeheader()
        writer.writerow(row)
    return LOG_FILE
