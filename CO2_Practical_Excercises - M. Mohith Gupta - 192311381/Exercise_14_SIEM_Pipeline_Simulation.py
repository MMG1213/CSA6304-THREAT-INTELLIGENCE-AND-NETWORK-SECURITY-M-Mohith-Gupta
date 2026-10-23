"""Exercise 14: Simulate collect, normalize, correlate, and alert SIEM stages."""
from collections import Counter
RAW_EVENTS=[
 {"source":"firewall","src_ip":"10.0.0.8","event":"failed_login","user":"admin"},
 {"source":"endpoint","src_ip":"10.0.0.8","event":"malware_detected","user":"admin"},
 {"source":"auth","src_ip":"10.0.0.8","event":"failed_login","user":"admin"},
 {"source":"firewall","src_ip":"10.0.0.9","event":"allowed_connection","user":"user1"}]
def normalize(event):
 return {k:str(event.get(k,"unknown")).lower() for k in ("source","event")} | {
  "src_ip":str(event.get("src_ip","unknown")),"user":str(event.get("user","unknown"))}
if __name__=="__main__":
 print("Step 1 — Collected raw events:",len(RAW_EVENTS))
 events=[normalize(e) for e in RAW_EVENTS]
 print("Step 2 — Normalized events:")
 for e in events: print(e)
 counts=Counter(e["src_ip"] for e in events)
 print("Step 3 — Event counts by source IP:",dict(counts))
 print("Step 4 — Alerts:")
 suspicious=[ip for ip in counts if sum(1 for e in events if e["src_ip"]==ip and e["event"] in {"failed_login","malware_detected"})>=2]
 if suspicious:
  for ip in sorted(suspicious): print(f"ALERT: Multiple suspicious events observed for {ip}")
 else: print("No alert raised.")
