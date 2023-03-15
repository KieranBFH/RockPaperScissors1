import random
ai = ["Rock", "Paper", "Scissors"]
p1 = " "
p2 = " "


def whowon():
    global p1
    p1.capitalize()
    global p2
    p2.capitalize()
    if p1 == p2:
        return(0)
    elif p1 == "Rock":
        if p2 == "Paper":
            return(2)
        elif p2 == "Scissors":
            return(1)
        else:
            return(-1)
    elif p1 == "Paper":
        if p2 == "Rock":
            return(1)
        elif p2 == "Scissors":
            return(2)
        else:
            return(-1)
    elif p1 == "Scissors":
        if p2 == "Rock":
            return(2)
        elif p2 =="Paper":
            return(1)
        else:
            return(-1)
    else:
        return(-1)


mode = input("Multiplayer or Singleplayer? (m/s): ")
if mode == 'm':
    p1 = input("Player 1: Rock Paper or Scissors? ")
    p2 = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer 2: Rock Paper or Scissors?  ")
    result = whowon()
    if result == -1:
        print('error')
    elif result == 0:
        print("Tie")
    elif result == 1:
        print("Player 1 Won")
    elif result == 2:
        print("Player 2 Won")

else:
    p1 = input("Player 1: Rock Paper or Scissors?")
    p2 = random.choice(ai)
    result = whowon()
    if result == -1:
        print('Error. Did you spell the options correctly?')
    elif result == 0:
        print("Tie! CPU played " + p2)
    elif result == 1:
        print("You won! CPU played" + p2)
    elif result == 2:
        print("You lost. CPU played " + p2)
