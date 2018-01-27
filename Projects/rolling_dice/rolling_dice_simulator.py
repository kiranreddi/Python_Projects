import random

def roll(sides=6):
    rolled = random.randint(1,sides)
    return rolled

def lets_roll():
    sides = 6
    rolling = True
    while rolling:
        roll_again = raw_input("Wanna Roll ? ENTER=Roll. Q=Quit. ")
        if roll_again.lower() != "q":
            rolled = roll(sides)
            print("You rolled a ", rolled)
        else:
            rolling = False

    print("Thanks for Playing")

lets_roll()
