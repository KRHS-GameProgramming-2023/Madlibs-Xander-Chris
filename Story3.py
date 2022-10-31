rom Getters import *

def Story3(debug = False):
    if debug: print("Story1 Function") 

    print("\n")
    friendName1 = getWord("Enter a name ", debug)
    LocationName = getWord("Enter a name", debug)
    MeatName = getWord("Enter a name", debug)
    SomethingFun = getWord("Enter a name", debug)
    
    
    
    
    
    
    out = "\n"
    out += "\n"
    out+= "me and my friend  " + friendName1
    out+= "are going to the " + LocationName
    out+= " for a pound of" + MeatName
    out+= " so we cane" + SomethingFun
    out+= "
    
    
    
    
    
    
    return out 

