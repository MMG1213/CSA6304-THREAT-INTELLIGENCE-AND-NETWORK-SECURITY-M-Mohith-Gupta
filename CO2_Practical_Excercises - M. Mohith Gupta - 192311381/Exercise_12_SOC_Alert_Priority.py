"""Exercise 12: Assign P1-P4 priority to a SOC alert."""
RULES=[
 ("P1",["ransomware","active data exfiltration","domain controller compromised","critical system down"]),
 ("P2",["privilege escalation","multiple hosts","confirmed malware","sensitive data exposure"]),
 ("P3",["suspicious login","malware blocked","repeated failed login","unusual activity"]),
 ("P4",["policy violation","low-risk","informational","single failed login"])]
def assign_priority(description):
 text=description.lower()
 for priority,keywords in RULES:
  if any(word in text for word in keywords): return priority
 return "Needs analyst review (no rule matched)"
if __name__=="__main__":
 print("Assigned priority:",assign_priority(input("Enter SOC alert description: ")))
