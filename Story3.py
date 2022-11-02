from Getters import *

def Story3(debug = False):
    if debug: print("Story1 Function") 

    print("\n")
    friendName1 = getWord("Enter a name ", debug)
    LocationName = getWord("Enter a location", debug)
    MeatName = getMeat("Enter a meat", debug)
    SomethingFun = getWord("Enter a somthing fun", debug)
    Activity = getWord("Enter a activity", debug)
    Emotion = getEmotion("Enter a emotion", debug)
    Emotion2 = getWord("Enter a emotion", debug)
    AThing = getWord("Enter a thing", debug)
    
    
    
    out = "\n"
    out += "\n"
    out+= "me and my friend  " + friendName1
    out+= " are going to the " + LocationName
    out+= " for a pound of" + MeatName
    out+= " so we can" + SomethingFun
    out+= " after we did that we " + Activity
    out+= " it was" + Emotion
    out+= " today was " + Emotion2
    out+= " im glad we did not " + AThing
    
    
    
    
    return out 

