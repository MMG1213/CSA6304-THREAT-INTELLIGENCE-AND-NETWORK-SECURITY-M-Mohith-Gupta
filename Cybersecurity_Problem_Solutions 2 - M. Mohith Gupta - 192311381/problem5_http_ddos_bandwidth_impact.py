"""
Problem 5 – DDoS Bandwidth Impact Calculation
Calculates request rate and theoretical bandwidth from supplied values.
This program does not generate HTTP requests or network traffic.
"""

devices = int(input("Enter number of compromised devices: "))
requests_per_device = float(input("Enter HTTP requests per device per second: "))
request_size_bytes = float(input("Enter average request size (bytes): "))
link_capacity_gbps = float(input("Enter target link capacity (Gbps): "))

if devices < 0 or requests_per_device < 0 or request_size_bytes < 0 or link_capacity_gbps <= 0:
    raise ValueError("Inputs must be non-negative and link capacity must be positive.")

request_rate = devices * requests_per_device
bytes_per_second = request_rate * request_size_bytes
bits_per_second = bytes_per_second * 8
bandwidth_mbps = bits_per_second / 1_000_000
bandwidth_gbps = bits_per_second / 1_000_000_000

saturation_factor = bandwidth_gbps / link_capacity_gbps
excess_gbps = max(0, bandwidth_gbps - link_capacity_gbps)
excess_percentage = max(0, (bandwidth_gbps - link_capacity_gbps) / link_capacity_gbps * 100)

print("\n--- Results ---")
print(f"(a) Total request rate: {request_rate:,.0f} requests/second")
print(f"(b) Incoming data rate: {bytes_per_second:,.0f} bytes/second")
print(f"    Bandwidth: {bandwidth_mbps:,.2f} Mbps = {bandwidth_gbps:.3f} Gbps")
print(f"(c) Saturation factor: {saturation_factor:.2f}x")
if bandwidth_gbps > link_capacity_gbps:
    print(f"    Link is saturated under the stated assumptions.")
    print(f"    Excess bandwidth: {excess_gbps:.3f} Gbps ({excess_percentage:.2f}%)")
else:
    print("    Offered traffic does not exceed link capacity.")

print("\nNote: This idealized estimate uses request payload size only. Actual traffic")
print("also includes protocol headers and may be affected by overhead and filtering.")
