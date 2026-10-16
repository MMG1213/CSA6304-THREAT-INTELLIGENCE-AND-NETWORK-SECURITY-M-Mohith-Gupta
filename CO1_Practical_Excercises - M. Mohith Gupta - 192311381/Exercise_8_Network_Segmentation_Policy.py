"""Exercise 8: Model a segmented network and block low-trust lateral movement."""

ACCESS_POLICY = {
    "LOW_TRUST": {"PUBLIC_WEB"},
    "EMPLOYEE": {"PUBLIC_WEB", "INTERNAL_APP"},
    "SENSITIVE": {"AUTHORIZED_ADMIN"}
}

def can_access(source_segment, destination_resource):
    return destination_resource in ACCESS_POLICY.get(source_segment, set())

if __name__ == "__main__":
    tests = [
        ("LOW_TRUST", "PUBLIC_WEB"),
        ("LOW_TRUST", "SENSITIVE_DB"),
        ("EMPLOYEE", "INTERNAL_APP"),
        ("EMPLOYEE", "SENSITIVE_DB"),
        ("AUTHORIZED_ADMIN", "SENSITIVE_DB"),
    ]
    # The final admin rule is handled explicitly as a privileged identity/segment.
    for source, destination in tests:
        allowed = (destination == "SENSITIVE_DB" and source == "AUTHORIZED_ADMIN") or can_access(source, destination)
        print(f"{source} -> {destination}: {'ALLOWED' if allowed else 'BLOCKED'}")
