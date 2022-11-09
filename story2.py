from Getters import *

def Story2(debug = False):
    if debug: print("Story2 Function") 

    print("\n")
    friendName1 = getWord("Enter a name ", debug)
    storeName = getstoreName("Enter a store name ", debug)
    kitchenAplience = getkitchenAplience("Enter a kichen applience ", debug)
    furniture = getfurniture("Enter a peice of furniture ", debug)
    vehical = getVehicle("Enter a mode of transportation ", debug)
    gasStationName = getGasStationName("Enter a gas station name ", debug)
    dscrp = getdscrp("Enter a word that you would use to describe how your day went ", debug)
 
    out ="\n"
    out+="\n"
    out+= " one day me and my friend " + friendName1
    out+= " went to a store called " + storeName
    out+= ". he decided to buy a " + kitchenAplience
    out+= " and then decided to get a " + furniture
    out+= ". there barly was enough space in the " + vehical
    out+= ". there was just enough gas to get to the closest " + gasStationName
    out+= ". the day was " + dscrp
     
    return out 



