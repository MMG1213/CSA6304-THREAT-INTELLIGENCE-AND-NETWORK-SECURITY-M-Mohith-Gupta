"""Exercise 10: Simulate a stateful inspection firewall."""
class StatefulFirewall:
 def __init__(self): self.connections=set()
 def outbound(self,source,destination,protocol="TCP"):
  self.connections.add((source,destination,protocol.upper()))
  return "ALLOWED - outbound connection recorded"
 def inbound(self,source,destination,protocol="TCP"):
  if (destination,source,protocol.upper()) in self.connections:
   return "ALLOWED - return traffic belongs to an established connection"
  return "BLOCKED - unsolicited inbound traffic"
if __name__=="__main__":
 fw=StatefulFirewall()
 print("Outbound 10.0.0.5 -> 203.0.113.10:",fw.outbound("10.0.0.5","203.0.113.10"))
 print("Return 203.0.113.10 -> 10.0.0.5:",fw.inbound("203.0.113.10","10.0.0.5"))
 print("Unsolicited 198.51.100.7 -> 10.0.0.5:",fw.inbound("198.51.100.7","10.0.0.5"))
