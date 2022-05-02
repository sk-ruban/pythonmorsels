from dataclasses import dataclass


# order allows for instance comparison
@dataclass(order=True)
class Month:
    year: int
    month: int

    def __str__(self):
        return f"{self.year}-{format(self.month, '02d')}"


# Base Problem
dec99 = Month(1999, 12)
print(dec99)
print(Month(1998, 12) == (1998, 12))
print(sorted([Month(1998, 12), Month(2000, 1), Month(1999, 12)]))

# Bonus 1
