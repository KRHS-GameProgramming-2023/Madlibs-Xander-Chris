from Getters import *

def Story1(debug = False):
    if debug: print("Story1 Function") 

    print("\n")
    friendName1 = getWord("Enter a name ", debug)
    sport1 = getSport("Enter a sport ", debug)
    bodyPart = getBodyPart("Enter a body part ", debug)
    medicalCondition = getWord("Enter a medical condition ", debug)
    baseLocation = getWord("Enter a base location ", debug)
    amountOfTime = getWord("Enter a amont of time ", debug)
    emotion1 = getEmotion("Enter a emotion ", debug)
    
    out = "\n"
    out += "\n"
    out+= "One day me and my friend " + friendName1
    out+= " Were out playing " + sport1
    out += " and he hurt his " + bodyPart
    out+= ".  He was " + medicalCondition
    out+= " he had to go to the " +baseLocation
    out+= ". he couldn't play for " +amountOfTime
    out+= " It was " + emotion1

    return out 



 
