
CURRENT_YEAR = 2024
VINTAGE_AGE = 100

class Guitar:
    """Guitar calss cor storing details of a guitar."""

    def __int__(self, name="", year=0, cost=0):
        """Initialise a Guitar."""
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
        """Compare guitars based on their year."""
        return self.year < other.year