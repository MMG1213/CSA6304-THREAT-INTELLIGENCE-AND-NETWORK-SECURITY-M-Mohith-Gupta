"""Exercise 1: Identify a threat-intelligence application area from a business scenario."""

def identify_application(scenario):
    scenario = scenario.lower()

    application_keywords = {
        "Banking Fraud Prevention": [
            "bank", "banking", "credit card", "debit card", "transaction",
            "fraud", "financial", "payment", "account takeover", "atm"
        ],
        "Healthcare Data Protection": [
            "hospital", "healthcare", "patient", "medical", "health record",
            "ehr", "clinical", "diagnosis", "patient data", "medical data"
        ],
        "E-Commerce Fraud Prevention": [
            "e-commerce", "ecommerce", "online shopping", "online store",
            "shopping", "retailer", "customer order", "checkout",
            "online payment", "product purchase", "fraudulent orders"
        ],
        "Cloud Security": [
            "cloud", "cloud service", "cloud storage", "virtual machine",
            "saas", "paas", "iaas"
        ],
        "Telecommunication Security": [
            "telecom", "telecommunication", "mobile network", "subscriber",
            "5g", "4g", "cellular", "network operator"
        ]
    }

    scores = {}
    for application, keywords in application_keywords.items():
        scores[application] = sum(1 for keyword in keywords if keyword in scenario)

    best_application = max(scores, key=scores.get)
    if scores[best_application] == 0:
        return "No specific Threat Intelligence application area identified."
    return best_application


if __name__ == "__main__":
    print("=== Threat Intelligence Application Area Identifier ===")
    scenario = input("Enter the business scenario: ")
    print("\\nMost Relevant Threat Intelligence Application Area:")
    print(identify_application(scenario))
