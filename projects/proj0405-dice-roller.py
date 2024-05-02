import random

def roll_die():
    return random.randint(1,6)

def main():
    print("Dice Roller\n")
    roll_choice = input("Roll the dice? ")
    while (roll_choice.lower()=="y"):
        die_1 = roll_die()
        die_2 = roll_die()
        display_die(die_1, die_2)
        print()
        roll_choice = input("Roll again? (y/n) ")

def display_die(die_1, die_2):
    print()
    print(f'Die 1: {die_1}')
    print(f'Die 2: {die_2}')
    sum = die_1 + die_2
    print(f'Total: {sum}')
    if (sum==2):
        print("Snake eyes!")
    elif (sum==12):
        print("Box Cars!")

if __name__ == "__main__":
    main()