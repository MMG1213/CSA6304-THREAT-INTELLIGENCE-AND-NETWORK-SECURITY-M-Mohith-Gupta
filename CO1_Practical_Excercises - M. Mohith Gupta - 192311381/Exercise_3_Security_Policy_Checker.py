"""Exercise 3: Check a draft security policy for required governance elements."""

REQUIRED_ELEMENTS = {
    "scope": ["scope", "applies to", "covered systems"],
    "roles and responsibilities": ["roles and responsibilities", "responsibilities", "owner"],
    "enforcement": ["enforcement", "disciplinary", "compliance checks"],
    "review cycle": ["review cycle", "reviewed annually", "annual review", "review every"],
    "approval authority": ["approval authority", "approved by", "authorised by", "authorized by"]
}

def check_policy(policy_text):
    text = policy_text.lower()
    present, missing = [], []
    for element, indicators in REQUIRED_ELEMENTS.items():
        if any(indicator in text for indicator in indicators):
            present.append(element)
        else:
            missing.append(element)
    return present, missing

if __name__ == "__main__":
    print("=== Security Policy Governance Checker ===")
    print("Paste policy text below. Enter a line containing only END to finish.")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "END":
            break
        lines.append(line)
    present, missing = check_policy("\\n".join(lines))
    print("\\nGovernance elements found:")
    print("\\n".join(f"- {item}" for item in present) if present else "- None")
    print("\\nMissing governance elements:")
    print("\\n".join(f"- {item}" for item in missing) if missing else "- None; all required elements appear to be present.")
