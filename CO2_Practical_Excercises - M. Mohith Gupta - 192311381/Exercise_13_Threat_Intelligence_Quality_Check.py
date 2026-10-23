"""Exercise 13: Check context, confidence, and actionability of collected data."""
def assess_data(context,confidence,actionability):
 missing=[]
 if not context.strip(): missing.append("context")
 if not 1<=confidence<=5: return "Invalid confidence: enter a value from 1 to 5."
 if confidence<3: missing.append("adequate confidence")
 if not actionability.strip(): missing.append("actionability")
 if missing: return "Raw/unprocessed data — missing or weak: "+", ".join(missing)
 return "Qualifies as threat intelligence: context, confidence, and actionability are present."
if __name__=="__main__":
 context=input("Enter context (source, target, or observed behavior): ")
 try: confidence=int(input("Confidence level (1-5): "))
 except ValueError: print("Confidence must be an integer from 1 to 5."); raise SystemExit(1)
 action=input("Enter a recommended defensive action: ")
 print(assess_data(context,confidence,action))
