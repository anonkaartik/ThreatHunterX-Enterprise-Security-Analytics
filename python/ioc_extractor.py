import pandas as pd

logs = pd.read_csv("C:\\Users\Anonymous\\OneDrive\\Attachments\\Desktop\\ThreatHunterX-Enterprise-Security-Analytics\\data\\security_logs.csv")

suspicious_ips = [
    "185.220.101.45",
    "45.33.32.156"
]

ioc_matches = logs[
    logs["source_ip"].isin(suspicious_ips)
]

print("\n=== IOC Detection Results ===\n")
print(ioc_matches)

print("\n=== Summary ===\n")
print(f"Total IOC Matches: {len(ioc_matches)}")

if len(ioc_matches) > 0:
    print("Threat Indicators Found")
else:
    print("No Threat Indicators Found")