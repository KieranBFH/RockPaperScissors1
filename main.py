import random
ai = ["r", "p", "c"]
mode = input("Select mode my g (m/s): ")
if mode == 'm':
    p1 = input("Player 1 Rock Paper or Scissors (r, p, s) ")
    p2 = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPlayer 2 Rock Paper or Scissors (r, p s) ")
else:
    p1 = input("Player 1 Rock Paper or Scissors (r, p, s) ")
    p2 = random.choice(ai)
    print("Player 2 choice randomized")

if p1 == p2:
    print("Tie")
elif p1 == "r":
    if p2 == "p":
        print("P2 Wins")
    elif p2 == "s":
        print("P1 Wins")
    else:
        print("error")
elif p1 == "p":
    if p2 == "r":
        print("P1 Wins")
    elif p2 == "s":
        print("P2 Wins")
    else:
        print('error')
elif p1 == "s":
    if p2 == "r":
        print("P2 Wins")
    elif p2 =="p":
        print("P1 Wins")
    else:
        print('error')
else:
    print('error')
