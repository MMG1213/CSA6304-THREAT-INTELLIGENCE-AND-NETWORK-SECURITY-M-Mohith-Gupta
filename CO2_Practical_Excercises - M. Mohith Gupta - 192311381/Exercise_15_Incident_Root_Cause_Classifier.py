"""Exercise 15: Classify a case study by likely security incident root cause."""
CATEGORIES={
 "Phishing":["phishing","fake login page","malicious email","clicked a link","credential theft"],
 "Unpatched vulnerability":["unpatched","missing security update","known vulnerability","outdated software","cve-"],
 "Misconfiguration":["misconfiguration","default password","publicly exposed","open storage bucket","incorrect permissions"],
 "Insider threat":["insider","employee copied","staff member stole","unauthorized employee access","malicious contractor"],
 "Supply-chain compromise":["supply chain","compromised vendor","third-party update","tampered dependency","vendor software"]}
def classify_incident(narrative):
 text=narrative.lower()
 scores={c:sum(1 for w in words if w in text) for c,words in CATEGORIES.items()}
 best=max(scores,key=scores.get)
 return best if scores[best] else "Root cause unclear; manual investigation required."
if __name__=="__main__":
 print("Likely root-cause category:",classify_incident(input("Enter the security incident case study: ")))
