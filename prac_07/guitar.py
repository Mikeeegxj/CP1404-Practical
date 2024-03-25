import csv

CURRENT_YEAR = 2024
VINTAGE_AGE = 100


class Guitar:
    """Guitar class for storing details of a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is considered vintage or not based on age."""
        return self.get_age() >= VINTAGE_AGE
    def __lt__(self, other):
        """Less than, for sorting guitars by year."""
        return self.year < other.year

def main():
    filename = 'guitars.csv'
    guitars = load_guitars_from_file(filename)

    print("These are the current guitars:")
    for guitar in guitars:
        print(guitar)

    while True:
        name = input("Enter the name of the guitar: ")
        if name == "":
            break
        year = int(input("Enter the year of the guitar: "))
        cost = float(input("Enter the cost of the guitar: "))
        guitars.append(Guitar(name, year, cost))

    guitars.sort()
    write_guitars_to_file(filename, guitars)


    print("These are the updated guitars:")
    updated_guitars = load_guitars_from_file(filename)
    for guitar in updated_guitars:
        print(guitar)

def load_guitars_from_file(filename):
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars



def write_guitars_to_file(filename, guitars):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

def load_guitars_from_file(filename):
    guitars = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for name, year, cost in reader:
                guitars.append(Guitar(name, int(year), float(cost)))
    except FileNotFoundError:
        print(f"No file named {filename} found. Starting with an empty list.")
    except ValueError:
        print("Error: Invalid data format in file.")
    return guitars



if __name__ == '__main__':
    main()
