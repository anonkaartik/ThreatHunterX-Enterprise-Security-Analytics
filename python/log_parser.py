import pandas as pd

logs = pd.read_csv("C:\\Users\Anonymous\\OneDrive\\Attachments\\Desktop\\ThreatHunterX-Enterprise-Security-Analytics\\data\\security_logs.csv")

failed_logins = logs[
    logs["event"] == "Failed Login"
]

critical_events = logs[
    logs["severity"] == "Critical"
]

print("\n=== Failed Login Events ===\n")
print(failed_logins)

print("\n=== Critical Security Events ===\n")
print(critical_events)

print("\n=== Statistics ===\n")
print(f"Failed Logins: {len(failed_logins)}")
print(f"Critical Events: {len(critical_events)}")