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

def isSwear (word, debug = False):
    if debug: print("isSwear Function")
    if word.lower() in swearList :
        return True
    else:
        return False



swearList =[ "poop",
            "pee"
]


















