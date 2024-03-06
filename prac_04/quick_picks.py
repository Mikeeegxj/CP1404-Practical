import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick picks program - choose random number"""
    number_of_quick_pick = int(input("How many quick picks? "))
    while number_of_quick_pick < 0:
        print("Invalid please enter again ")
        number_of_quick_pick = int(input("How many quick picks? "))

    for i in range(number_of_quick_pick):
        quick_pick = []
        for g in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


main()