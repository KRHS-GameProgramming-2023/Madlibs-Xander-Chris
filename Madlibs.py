from Screens import *
from Getters import *
from Story1 import *




def Madlibs (debug = False):
    if debug: print ("welcome to debug")
    
    print(TitleScreen(debug))
    input ("press enter to continue")

    done = False
    
    while not done:
        print(MainMenu(debug))
        choice = getMenuOption(debug)
       
        if choice == "q":
            exit();
            
        elif choice == "1":
            print(Story1())
            print("\n") 
            input("press enter to continue")
            
            
            
            






Madlibs (False)

