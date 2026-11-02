"""
Problem 4 – IoC and Threat Feed Correlation
Demonstrates defensive correlation using fictional/sample log events.
No real IP, domain, or malware file is contacted or executed.
"""

from datetime import datetime

# Example indicators from a threat feed (use authorized, trusted feed data in practice).
threat_feed = {
    "malicious_ips": {"203.0.113.10"},
    "malicious_domains": {"malware-example.invalid"},
    "malicious_hashes": {"a" * 64},
    "published_at": datetime.strptime("09:00", "%H:%M"),
}

# Sample SIEM/endpoint events corresponding to the scenario in the question.
events = [
    {
        "time": "08:50",
        "type": "login",
        "source_ip": "203.0.113.10",
        "description": "Login observed from an IP later listed in the threat feed",
    },
    {
        "time": "09:05",
        "type": "file_created",
        "sha256": "a" * 64,
        "description": "File created on a workstation; hash later matched the feed",
    },
]

investigation_time = datetime.strptime("09:15", "%H:%M")
published_at = threat_feed["published_at"]

print("IOC / Threat Feed Correlation Report")
print("=" * 48)
print(f"Threat feed published: {published_at.strftime('%H:%M')}")
print(f"Investigation time:    {investigation_time.strftime('%H:%M')}\n")

for event in events:
    event_time = datetime.strptime(event["time"], "%H:%M")
    matches = []

    if event.get("source_ip") in threat_feed["malicious_ips"]:
        matches.append("malicious IP")
    if event.get("domain") in threat_feed["malicious_domains"]:
        matches.append("malicious domain")
    if event.get("sha256") in threat_feed["malicious_hashes"]:
        matches.append("malicious file hash")

    print(f"[{event['time']}] {event['type']}: {event['description']}")
    if matches:
        print("  IOC match:", ", ".join(matches))
        if event_time < published_at:
            print("  Timing: Event occurred BEFORE feed publication (retrospective match).")
        else:
            print("  Timing: Event occurred AFTER feed publication.")
    else:
        print("  IOC match: No match in the supplied indicators.")
    print()

print("Recommended defensive actions:")
print("1. Investigate the account, authentication result, source IP, and later activity.")
print("2. Follow incident-response procedures to isolate the affected workstation.")
print("3. Quarantine the suspected file using endpoint security tools; do not execute it.")
print("4. Preserve forensic evidence and inspect process activity and persistence.")
print("5. Search historical DNS, proxy, firewall, SIEM, and endpoint logs for all IoCs.")
print("6. Validate threat-feed ingestion and alerting to prevent future delays.")
print("\nCaution: An IOC match is an alert for investigation; it does not alone prove")
print("successful account compromise or malware execution.")
