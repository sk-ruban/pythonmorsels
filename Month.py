from dataclasses import dataclass
import calendar
from datetime import date


# order allows for instance comparison
# frozen allows for instance immutability
@dataclass(order=True, frozen=True)
class Month:
    # __slots__ explicitly state which instance attributes you expect your object instances to have
    # Allows for space savings!
    __slots__ = ('year', 'month')
    year: int
    month: int

    @property
    def first_day(self):
        return date(self.year, self.month, 1)

    @property
    def last_day(self):
        first, last = calendar.monthrange(self.year, self.month)
        return date(self.year, self.month, last)

    def __str__(self):
        return f"{self.year}-{format(self.month, '02d')}"

    @classmethod
    def from_date(cls, date):
        return cls(date.year, date.month)

    def strftime(self, syntax):
        # Cheating because I used 1 as a faux-day since date() requires 3 arguments
        return date(self.year, self.month, 1).strftime(syntax)


# Base Problem
dec99 = Month(1999, 12)
print(dec99)
print(Month(1998, 12) == (1998, 12))
print(sorted([Month(1998, 12), Month(2000, 1), Month(1999, 12)]))

# Bonus 1
print(dec99.first_day)
print(dec99.last_day)

# Bonus 2
nye99 = date(1999, 12, 31)
dec99 = Month.from_date(nye99)
print(dec99)
dec99.strftime('%b %Y')

# Bonus 3
dec99 = Month(1999, 12)
dec99.year = 1998