import random
ai = ["r", "p", "c"]
p1 = " "
p2 = " "
def whowon():
    global p1
    global p2
    if p1 == p2:
        return(0)
    elif p1 == "r":
        if p2 == "p":
            return(2)
        elif p2 == "s":
            return(1)
        else:
            return(-1)
    elif p1 == "p":
        if p2 == "r":
            return(1)
        elif p2 == "s":
            return(2)
        else:
            return(-1)
    elif p1 == "s":
        if p2 == "r":
            return(2)
        elif p2 =="p":
            return(1)
        else:
            return(-1)
    else:
        return(-1)

mode = input("Select mode my g (m/s): ")
if mode == 'm':
    p1 = input("Player 1 Rock Paper or Scissors (r, p, s) ")
    p2 = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer 2 Rock Paper or Scissors (r, p s) ")
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
    p1 = input("Player 1 Rock Paper or Scissors (r, p, s) ")
    p2 = random.choice(ai)
    result = whowon()
    if result == -1:
        print('error')
    elif result == 0:
        print("Tie")
    elif result == 1:
        print("You won!")
    elif result == 2:
        print("You lost.")
