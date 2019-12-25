VINTAGE_AGE = 50
class Guitar:#this class stores basic information of the guitar

    def __init__(self, name="", year=0, cost=0):
        self.name=name
        self.year=year
        self.cost=cost

    def __str__(self):#returns a string of the information of the guitar
        return "{} ({}): ${:,.2f}".format(self.name,self.year,self.cost)

    def get_age(self):
        return 2019-self.year

    def is_vintage(self):#determines whether the guitar is vintage depending on the age of the guitar
        return self.get_age()>=VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year released."""
        return self.year < other.year