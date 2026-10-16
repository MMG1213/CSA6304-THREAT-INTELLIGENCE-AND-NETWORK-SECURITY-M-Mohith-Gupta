"""Exercise 6: Flag possible phishing URLs using simple heuristic indicators.
This is a learning aid and may produce false positives/negatives.
"""
import ipaddress
from urllib.parse import urlparse

SUSPICIOUS_KEYWORDS = ["login", "verify", "update", "secure", "account", "password", "confirm", "wallet"]

def detect_phishing(url):
    candidate = url.strip()
    if "://" not in candidate:
        candidate = "http://" + candidate
    parsed = urlparse(candidate)
    host = parsed.hostname or ""
    indicators = []

    if parsed.scheme.lower() != "https":
        indicators.append("URL does not use HTTPS")
    if any(word in candidate.lower() for word in SUSPICIOUS_KEYWORDS):
        indicators.append("Contains a common sensitive-action keyword")
    try:
        ipaddress.ip_address(host)
        indicators.append("Uses an IP address instead of a domain name")
    except ValueError:
        pass
    if len([part for part in host.split(".") if part]) > 3:
        indicators.append("Has excessive subdomains")
    if "@" in parsed.netloc:
        indicators.append("Contains @ in the network location")

    return indicators

if __name__ == "__main__":
    url = input("Enter a URL to check: ")
    findings = detect_phishing(url)
    if findings:
        print("\\nWarning: suspicious indicators found:")
        for finding in findings:
            print("-", finding)
        print("Result: Potentially suspicious; verify independently.")
    else:
        print("\\nNo indicators from this simple checklist were detected.")
    print("Note: This heuristic is not a definitive phishing verdict.")
