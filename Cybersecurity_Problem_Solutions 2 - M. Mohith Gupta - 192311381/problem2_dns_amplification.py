"""
Problem 2 – DNS Amplification Attack Calculation
A calculator only; it does not send DNS queries or generate network traffic.
"""

query_size = float(input("Enter DNS query size (bytes): "))
response_size = float(input("Enter DNS response size (bytes): "))
query_bandwidth_mbps = float(input("Enter outbound query bandwidth (Mbps): "))

if query_size <= 0 or response_size < 0 or query_bandwidth_mbps < 0:
    raise ValueError("Sizes and bandwidth must be non-negative; query size must be positive.")

amplification_factor = response_size / query_size
effective_bandwidth_mbps = query_bandwidth_mbps * amplification_factor

print("\n--- Results ---")
print(f"Amplification factor: {amplification_factor:.2f}x")
print(f"Theoretical effective bandwidth: {effective_bandwidth_mbps:.2f} Mbps")
print(f"In Gbps: {effective_bandwidth_mbps / 1000:.3f} Gbps")
print("Note: This is a theoretical calculation. Real throughput may be lower due to")
print("protocol overhead, resolver limits, filtering, and network constraints.")
