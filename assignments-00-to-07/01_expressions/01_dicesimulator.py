import random

SIDES_IN_DIE = 6

def roll_dice():

    die1: int = random.randint(1, SIDES_IN_DIE)
    die2: int = random.randint(1, SIDES_IN_DIE)
    total: int = die1 + die2
    print("Total of two dice:", total)

def main():
    roll_dice()
    roll_dice()
    roll_dice()

if __name__ == '__main__':
    main()