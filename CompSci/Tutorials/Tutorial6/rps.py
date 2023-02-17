import random

choice = int(input("\n0. Rock \n1. Paper \n2. Scissors: \n"))


if choice == 0:
    counter = random.randint(0,2)
    print("You Chose To Play Rock")
    if counter == choice:
        print("Your Opponent Picked Rock Also.... #DRAW")
    elif counter == 1:
        print("Your Opponent Picked Paper- YOU LOSE LMFAO!!!!!")
    else:
        print("Your Opponent Picked Scissors- YOU WON")
if choice == 1:
    print("You Chose To Play Paper")
    counter = random.randint(0,2)
    if counter == choice:
        print("Your Opponent Also Chose Paper... #DRAW")
    elif counter == 2:
        print("OOF- Your Opponent Choose Scissors- YOU LOSE LMFAO!!!!!")
    else:
        print("Welp, Your Opponent Chose Rock- SO you WON")
if choice == 2:
    print("You Chose To Play Scissors")
    counter = random.randint(0,2)
    if counter == choice:
        print("Your Opponent Picked Scissiors so...this is awkward...#DRAW")
    elif counter == 0:
        print("Your Opponent Picked Rock! YOU LOSE LMFAO!!!!!")
    else:
        print("Your opponent picked Paper- SO YOU WON!")