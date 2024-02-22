

MENU = """1 - Celsius to Fahrenheit\n2- Fahrenheit to Celsius\n3 - Quit"""


def main():
    """Temperature conversion program."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "3":
        if choice == "1":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        elif choice == "2":
            fahrenheit = float(input("Fahrenheit : "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        else:
            print("Invalid choice. Please select 1 or 2 or 3.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

main()
