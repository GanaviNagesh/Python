# We all have played snake, water gun game in our childhood write a python prograam capable of playing this game withe user
import random
    

def play(playing):
        while(playing):
            comuterchoice=random.choice(["snake","water","gun"])
            Human=input("enter your choice snake,water or gun: ")
            if(comuterchoice=="snake" and Human=="water" or comuterchoice=="water" and Human=="gun" or comuterchoice=="gun" and Human=="snake"):
                print(f"computer choose {comuterchoice} so computer won!!! and human lost :< :(")
                print("comuter choice wins")
                
            if(Human=="snake" and comuterchoice=="water" or Human=="water" and comuterchoice=="gun" or Human=="gun" and comuterchoice=="snake"):
                print(f"computer choose {comuterchoice} so computer lost:(:< and human wom:> and :)")
                print("Human wins")
                
            if(comuterchoice==Human):
                print(f"computer choose {comuterchoice}")
                print("its a DRAW between both")
            val=int(input("play again then 1 else 0: "))
            playing=val
            
        

play(True)


