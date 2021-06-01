# Snake Water Gun Game. or Rock Paper Scissor


import random


def gameWin(comp, player):
    if (comp==player):          # if Two values are equal then it's tie
        return None

        #checking possibilitie when computer chose s
    elif(comp=="s" and player=="w"):
        return False
    elif(comp=="s" and player=="g"):
        return True

        #checking possibilitie when computer chose w
    elif(comp=="w" and player=="g"):
        return False
    elif(comp=="w" and player=="s"):
        return True

        #checking possibilitie when computer chose g
    elif(comp=="g" and player=="s"):
        return False
    elif(comp=="g" and player=="w"):
        return True





print("Computer Turn : Snake(s) Water(w) Gun(g)?")
Rnum=random.randint(1,3)
if Rnum==1:
    comp="s"

elif Rnum==2:
    comp="w"


elif Rnum==3:
    comp="g"
player=input("Player2 Turn : Snake(s) Water(w) Gun(g)?")

a=gameWin(comp,player)

print(f"Computer Chose : {comp}")
print(f"Player Chose : {player}")

if(a==None):
    print("The Game is a Tie")

elif a:
    print("You Win!!!")

else:
    print("So Sad, You Lost")

