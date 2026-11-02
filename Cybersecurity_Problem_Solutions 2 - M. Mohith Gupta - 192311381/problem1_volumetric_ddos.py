"""
Problem 1 – Volumetric DDoS Bandwidth Calculation
Calculates offered attack bandwidth and compares it with link capacity.
"""

devices = int(input("Enter number of compromised IoT devices: "))
bandwidth_per_device = float(input("Enter attack bandwidth per device (Mbps): "))
link_capacity_gbps = float(input("Enter victim link capacity (Gbps): "))

attack_mbps = devices * bandwidth_per_device
attack_gbps = attack_mbps / 1000
capacity_mbps = link_capacity_gbps * 1000
excess_gbps = max(0, attack_gbps - link_capacity_gbps)
excess_percentage = max(0, (attack_gbps - link_capacity_gbps) / link_capacity_gbps * 100)

print("\n--- Results ---")
print(f"Total attack bandwidth: {attack_mbps:,.2f} Mbps = {attack_gbps:.2f} Gbps")
print(f"Victim link capacity:   {link_capacity_gbps:.2f} Gbps")
if attack_gbps > link_capacity_gbps:
    print(f"Excess bandwidth:       {excess_gbps:.2f} Gbps")
    print(f"Above link capacity:    {excess_percentage:.2f}%")
    print("Result: The offered traffic exceeds link capacity.")
else:
    print("Result: The offered traffic does not exceed link capacity.")

print("Assumption: All devices transmit simultaneously and traffic reaches the victim link.")
