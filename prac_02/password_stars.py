
MINIMUM_LENGTH = 4

def main():
    """Get and print password using functions."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Get password, ensuring it meets the minimum_length requirement."""
    password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    while len(password) < minimum_length:
        print("Password too short")
        password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    return password


def print_asterisks(sequence):
    """Print as many asterisks as there are characters in the passed-in sequence."""
    print('*' * len(sequence))
