import random
print("rock, paper, or scissors")
def calculation():
    random.randrange(1, 3)
def rockpaperscissors():
    if input() == "rock":
        if calculation == 1:
            print("rock, draw!")
        elif calculation == 2:
            print("paper, I win!")
        else:
            print("scissors ,Nooo I lost!")
    #if you want to type paper, type paper 2 times since it is an elif condition
    elif input() == "paper":
        if calculation == 1:
            print("rock, Nooo I lost!")
        elif calculation == 2:
            print("Paper, Draw!")
        else:
            print("Scissors, Haha I got you!")
    #same goes here, type it 3 times if you want it to be scissors
    elif input() == "scissors":
        if calculation == 1:
            print("rock, Haha I got you!")
        elif calculation == 2:
            print("paper, Noo I lost!")
        else:
            print("Scissors, Draw!")
rockpaperscissors()



