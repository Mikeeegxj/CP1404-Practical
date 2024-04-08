import csv
from guitar import Guitar


def main():
    filename = 'guitars.csv'
    guitars = load_guitars(filename)

    print("Current guitars:")
    for guitar in guitars:
        print(guitar)


    add_new_guitars(guitars)


    guitars.sort(key=lambda g: g.year)


    print("Guitars sorted by year:")
    for guitar in guitars:
        print(guitar)


    save_guitars(filename, guitars)


def load_guitars(filename):
    """Load guitars from a given filename."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            name, year, cost = row
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def add_new_guitars(guitars):
    """Allow the user to add new guitars."""
    while True:
        name = input("Enter the name of the guitar (or enter to finish): ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))


def save_guitars(filename, guitars):
    """Save the list of guitars to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Year', 'Cost'])  # header
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])


if __name__ == '__main__':
    main()
