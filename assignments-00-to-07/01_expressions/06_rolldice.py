import random

def main():

    sides_of_dice = 6

    dice1 = random.randint(1, sides_of_dice)

    dice2 = random.randint(1, sides_of_dice)

    sum = dice1 + dice2

    print(f"Number on first Dice = {dice1}")
    print(f"Number on second Dice = {dice2}")
    print(f"The sum of both numbers = {sum}")


if __name__ == '__main__':
    main()