
def get_valid_score():
    """Prompt the user for a valid score between 0 and 100."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score. Score must be between 0 and 100.")
        score = float(input("Enter score: "))
    return score


def print_result(score):
    """Print the result based on the score."""
    if score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    print(f"Result: {result}")


def show_stars(score):
    """Print stars equal to the score."""
    stars = '*' * int(score)
    print(stars)


MENU = """(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"""


def main():
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == 'G':
            score = get_valid_score()
        elif choice == 'P':
            print_result(score)
        elif choice == 'S':
            show_stars(score)
        else:
            print("Invalid choice. Please choose again.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

main()

