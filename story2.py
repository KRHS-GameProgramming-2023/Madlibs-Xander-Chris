from Getters import *

def Story2(debug = False):
    if debug: print("Story2 Function") 

    print("\n")
    friendName1 = getWord("Enter a name ", debug)
    storeName = getWord("Enter a store name ", debug)
    kitchenAplience = getWord("Enter a kichen applience ", debug)
    furniture = getWord("Enter a peice of furniture ", debug)
    vehical = getWord("Enter a vehical ", debug)
 
 
 
    out ="\n"
    out+="\n"
    out+= " one day me annd my friend " + friendName1
    out+= " went to a stre called " + storeName
    out+= ". he decided to buy a " + kitchenAplience
    out+= " and then decided to get a " + furniture
    out+= ". there barly was enough space in the " + vehical
    out+= ". "
    out+=""
     
    return out 



