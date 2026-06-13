import csv
import random
from datetime import datetime, timedelta
events = [
    ("Failed Login", "Medium"),
    ("Successful Login", "Low"),
    ("PowerShell Execution", "High"),
    ("Privilege Escalation", "Critical"),
    ("Command and Control Connection", "Critical"),
    ("Credential Dumping", "Critical")
]
users = [
    "john.smith",
    "admin",
    "alice",
    "michael",
    "service.account"
]
ips = [
    "185.220.101.45",
    "192.168.1.25",
    "10.0.0.15",
    "45.33.32.156",
    "172.16.5.100"
]
start_time = datetime.now()
with open("C:\\Users\Anonymous\\OneDrive\\Attachments\\Desktop\\ThreatHunterX-Enterprise-Security-Analytics\\data\\security_logs.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([
        "timestamp",
        "user",
        "source_ip",
        "event",
        "severity"
    ])
    for i in range(100):
        event, severity = random.choice(events)
        timestamp = (
            start_time +
            timedelta(minutes=i)
        ).strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([
            timestamp,
            random.choice(users),
            random.choice(ips),
            event,
            severity
        ])
print("100 security events generated successfully.")
