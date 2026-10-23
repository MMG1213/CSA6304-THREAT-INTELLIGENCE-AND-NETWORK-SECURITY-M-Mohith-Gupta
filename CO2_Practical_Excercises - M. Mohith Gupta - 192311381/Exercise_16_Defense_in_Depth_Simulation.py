"""Exercise 16: Model an attack moving through ordered security layers."""
def evaluate_attack(attack,layers):
 print("Attack scenario:",attack)
 for name,blocks in layers:
  if blocks:
   print(f"{name}: BLOCKED the attack")
   print("Result: Attack did not reach the protected asset.")
   return
  print(f"{name}: Attack passed this layer")
 print("Result: Attack reached the protected asset; review the controls.")
if __name__=="__main__":
 print("=== Defense-in-Depth Simulation ===")
 evaluate_attack("Malicious attachment delivered by email",[
  ("Email security gateway",False),("Endpoint detection",True),
  ("Network firewall",False),("Access control",False)])
 print("\nSecond scenario — no layer blocks the attack:")
 evaluate_attack("Simulated attack with failed controls",[
  ("Email security gateway",False),("Endpoint detection",False),
  ("Network firewall",False),("Access control",False)])
