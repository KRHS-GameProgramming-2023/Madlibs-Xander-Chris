def getMenuOption(debug = False):
    if debug: print("getMenuOption Function")
    
    goodInput = False
    
    while not goodInput:
        option = input("please select an option: ")
        option = option.lower()
        
        if (option == "q" or 
            option == "quit" or 
            option == "x" or
            option == "exit"):
                option = "q"
                goodInput = True
                
        elif (option == "1" or 
            option == "story 1" or 
            option == "story1" or 
            option == "one" or
            option == "story one"):
                option = "1"
                goodInput = True
                
        elif (option == "2" or 
            option == "story 2" or 
            option == "story2" or 
            option == "two" or
            option == "story 2"):
                option = "2"
                goodInput = True

        elif (option == "3" or 
            option == "story 3" or 
            option == "story3" or 
            option == "three" or
            option == "story three"):
                option = "3"
                goodInput = True
                        
        elif (option == "u"):
                option = "unicorn"
                goodInput = True
            
        else:
            print ("please make a valid choice: ")
            
    return option   

def getWord(prompt, debug = False):
    if debug: print("getMenuOption Function")
    
    goodInput = False
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear (word):
            goodInput= False
            print ("don't use language like that")
        
    return word  
    
def getSport(prompt, debug = False):
    if debug: print("getgetSport Function")
    
    goodInput = False
    
    sports = ["soccer",
              "football",
              "hockey",
              "wrestling",
              "field hockey",
              "skiing",
              "nordic"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear (word):
            goodInput= False
            print("\n")
            print ("don't use language like that")
        elif word.lower() not in sports:
            goodInput= False
            print("\n")
            print ("sorry, I don't know that sport.")
        
    return word  
    
def getMeat(prompt, debug = False):
    if debug: print("getgetMeat Function")
    
    goodInput = False
    
    meats = ["bacon",
              "staek",
              "chicken",
              "beef",
              "spam",
              "fish",
              "squid"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear (word):
            goodInput= False
            print("\n")
            print ("don't use language like that")
        elif word.lower() not in meats:
            goodInput= False
            print("\n")
            print ("sorry, I don't know that meat.")
        
    return word  
    
    
    
    
    
def getEmotion(prompt, debug = False):
    if debug: print("getgetEmotion Function")
    
    goodInput = False
    
    meats = ["happy",
              "sad",
              "mad",
              "disgusted",
              "scared",
              "fear",
              "lol"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear (word):
            goodInput= False
            print("\n")
            print ("don't use language like that")
        elif word.lower() not in emotions:
            goodInput= False
            print("\n")
            print ("sorry, I don't know that emotion.")
        
    return word  
    
def getBodyPart(prompt, debug = False):
    if debug: print("getgetSport Function")
    
    goodInput = False
    
    bodyParts = ["hand",
              "foot",
              "head",
              "knee",
              "elbow",
              "jaw"]
    
    while not goodInput:
        word = input(prompt)
        goodInput = True
        if isSwear (word):
            goodInput= False
            print("\n")
            print ("don't use language like that")
        elif word.lower() not in bodyParts:
            goodInput= False
            print("\n")
            print ("sorry, I don't know that body part.")
        
    return word  

def isSwear (word, debug = False):
    if debug: print("isSwear Function")
    if word.lower() in swearList :
        return True
    else:
        return False



swearList =[ "poop",
            "pee"
]


















