# Attack Scenarios

## Scenario 1: Brute Force Attack

### Description

An attacker performs multiple failed login attempts against a user account before successfully gaining access.

### Indicators

* Multiple failed logins
* Successful login after failures
* Unusual source IP

### Severity

High

---

## Scenario 2: Privilege Escalation

### Description

A compromised user account gains administrative privileges.

### Indicators

* New admin group membership
* Privilege changes
* Elevated commands executed

### Severity

Critical

---

## Scenario 3: Suspicious PowerShell Activity

### Description

An attacker executes PowerShell commands for reconnaissance and persistence.

### Indicators

* PowerShell execution
* Encoded commands
* Script downloads

### Severity

High

---

## Scenario 4: Command and Control Communication

### Description

An infected host communicates with an external malicious server.

### Indicators

* Repeated outbound connections
* Suspicious domains
* Unusual traffic patterns

### Severity

Critical

---

## Scenario 5: Credential Access

### Description

An attacker attempts to dump credentials from the system.

### Indicators

* Mimikatz execution
* LSASS access
* Credential dumping tools

### Severity

Critical
