class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Initialise a programming language.
                For name, typing, reflection and year."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determines whether the language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Returns a string of the representation of ProgrammingLanguage."""
        return "{}, {}, Reflection={}, First appeared in {}.".format(self.name, self.typing, self.reflection, self.year)
