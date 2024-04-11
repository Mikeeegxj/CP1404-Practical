class Band:
    """Band class to manage a collection of musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band with its musicians and their instruments."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add_musician(self, musician):
        """Add a Musician to the Band's list of musicians."""
        self.musicians.append(musician)

    def play(self):
        """Have each Musician in the Band play their instrument."""
        for musician in self.musicians:
            print(musician.play())


