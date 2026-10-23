"""Exercise 9: Tag an activity with a Threat Intelligence Lifecycle stage."""
STAGES = {
 "Direction": ["requirements","priority intelligence requirement","pir","objective","what do we need to know"],
 "Collection": ["collect","gather","retrieve","logs","feeds","sources","obtain data"],
 "Processing": ["parse","clean","deduplicate","normalize","format","enrich data"],
 "Analysis": ["analyze","investigate","correlate","interpret","assess","determine impact"],
 "Dissemination": ["share","distribute","report","brief","send findings","publish"],
 "Feedback": ["feedback","review usefulness","request changes","improve requirements","stakeholder response"]
}
def tag_activity(description):
 text=description.lower()
 scores={stage:sum(1 for word in words if word in text) for stage,words in STAGES.items()}
 best=max(scores,key=scores.get)
 return best if scores[best] else "Stage unclear from the supplied description."
if __name__=="__main__":
 activity=input("Describe the intelligence-team activity: ")
 print("Lifecycle stage:",tag_activity(activity))
