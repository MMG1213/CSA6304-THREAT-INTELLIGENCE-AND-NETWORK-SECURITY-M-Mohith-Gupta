"""Exercise 5: Classify threat-intelligence reports as Strategic, Tactical, or Operational."""

KEYWORDS = {
    "Strategic": ["executive", "business impact", "long-term", "investment", "risk posture", "leadership", "policy"],
    "Tactical": ["tactics", "techniques", "procedures", "ttp", "mitre", "campaign", "tooling", "attacker method"],
    "Operational": ["ip address", "domain", "hash", "ioc", "indicator", "specific host", "malicious url", "timestamp"]
}

def classify_report(description, audience):
    text = (description + " " + audience).lower()
    scores = {category: sum(1 for keyword in words if keyword in text)
              for category, words in KEYWORDS.items()}
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        return "Unable to classify from the supplied keywords."
    return best

if __name__ == "__main__":
    description = input("Enter the threat-intelligence report description: ")
    audience = input("Enter the intended audience: ")
    print("\\nReport classification:", classify_report(description, audience))
