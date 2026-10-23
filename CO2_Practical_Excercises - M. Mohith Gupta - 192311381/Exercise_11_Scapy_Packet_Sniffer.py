"""Exercise 11: Scapy packet sniffer. Use only on networks you may monitor.
Install: python -m pip install scapy. Windows may require Npcap/admin privileges.
"""
try:
 from scapy.all import sniff
except ImportError:
 print("Scapy is not installed. Install it with: python -m pip install scapy")
 raise SystemExit(1)
def show_packet(packet): print(packet.summary())
if __name__=="__main__":
 interface=input("Interface name (press Enter for default): ").strip() or None
 try:
  count=int(input("Number of packets to capture (1-100): "))
  if not 1<=count<=100: raise ValueError
 except ValueError:
  print("Please enter a number from 1 to 100."); raise SystemExit(1)
 print("Starting authorized packet capture...")
 sniff(iface=interface,prn=show_packet,count=count,store=False)
 print("Capture complete.")
