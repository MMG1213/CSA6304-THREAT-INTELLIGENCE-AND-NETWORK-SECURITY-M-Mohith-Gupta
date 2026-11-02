"""
Problem 3 – CVSS-Based Vulnerability Prioritization
Classifies CVSS v3 base scores and prints findings in descending priority.
"""

findings = [
    ("Outdated SSL certificate", 3.1),
    ("Public-facing remote code execution flaw", 9.8),
    ("Default admin credentials on internal printer", 6.5),
    ("Missing security header on internal application", 2.0),
]

def severity(score):
    if score == 0:
        return "None"
    if 0 < score < 4.0:
        return "Low"
    if score < 7.0:
        return "Medium"
    if score < 9.0:
        return "High"
    return "Critical"

print("CVSS v3 Severity Bands")
print("0.0 = None | 0.1–3.9 = Low | 4.0–6.9 = Medium")
print("7.0–8.9 = High | 9.0–10.0 = Critical\n")

ranked = sorted(findings, key=lambda item: item[1], reverse=True)
print("Vulnerability".ljust(58), "Score".rjust(7), "Severity")
print("-" * 82)
for name, score in ranked:
    print(name.ljust(58), f"{score:>7.1f}", severity(score))

print("\nSuggested patching priority:")
for position, (name, score) in enumerate(ranked, start=1):
    print(f"{position}. {name} — {score:.1f} ({severity(score)})")

print("\nNote: CVSS is one prioritization input. Also consider exploitability,")
print("exposure, business impact, and compensating controls.")
