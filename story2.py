from Getters import *

def Story2(debug = False):
    if debug: print("Story2 Function") 

    print("\n")
    friendName1 = getWord("Enter a name ", debug)
    storeName = getWord("Enter a store name ", debug)
    kitchenAplience = getWord("Enter a kichen applience ", debug)
    furniture = getWord("Enter a peice of furniture ", debug)
    vehical = getWord("Enter a vehical ", debug)
    gasStationName = getWord("Enter a gas station name ", debug)
    dscrp = getWord("Enter a description word ", debug)
 
    out ="\n"
    out+="\n"
    out+= " one day me and my friend " + friendName1
    out+= " went to a store called " + storeName
    out+= ". he decided to buy a " + kitchenAplience
    out+= " and then decided to get a " + furniture
    out+= ". there barly was enough space in the " + vehical
    out+= ". there wsa just enough gas to get to the " + gasStationName
    out+= ". the day was very " + dscrp
     
    return out 



