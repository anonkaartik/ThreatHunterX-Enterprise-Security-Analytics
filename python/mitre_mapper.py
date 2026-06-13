import pandas as pd

logs = pd.read_csv("C:\\Users\Anonymous\\OneDrive\\Attachments\\Desktop\\ThreatHunterX-Enterprise-Security-Analytics\\data\\security_logs.csv")

mitre_mapping = {
    "Failed Login": "T1110 - Brute Force",
    "Successful Login": "T1078 - Valid Accounts",
    "PowerShell Execution": "T1059.001 - PowerShell",
    "Privilege Escalation": "T1068 - Exploitation for Privilege Escalation",
    "Command and Control Connection": "T1071 - Application Layer Protocol",
    "Credential Dumping": "T1003 - OS Credential Dumping"
}

logs["MITRE_Technique"] = logs["event"].map(mitre_mapping)

print("\n=== MITRE ATT&CK Mapping Results ===\n")
print(logs[["event", "MITRE_Technique"]].drop_duplicates())

logs.to_csv("C:\\Users\\Anonymous\\OneDrive\\Attachments\\Desktop\\ThreatHunterX-Enterprise-Security-Analytics\\data\\security_logs_mapped.csv", index=False)

print("\nMapping completed successfully.")

