import cmath
import decimal
from decimal import Decimal


def is_perfect_square(num, complex=False):
    # Bonus 3 - Complex numbers
    if complex:
        root = cmath.sqrt(num)
        return root.real.is_integer() and root.imag.is_integer()
    if type(num) is not str:
        if num > 0:
            num = Decimal(num)
            # Bonus 2 - Set the precision to handle bigger numbers
            decimal.getcontext().prec = 50
            return num.sqrt() % 1 == 0
        # Bonus 1 - Returns False if negative
        else:
            return False
    else:
        raise TypeError(f"Please input numbers")


is_perfect_square(1)
is_perfect_square(64.0)
is_perfect_square(65)
is_perfect_square(100)
is_perfect_square(1000)

square_number = Decimal('100')
is_perfect_square(square_number)

is_perfect_square(4624000000000000)
is_perfect_square(4623999999999999)
is_perfect_square(8383828483252752341748234**2-1)

is_perfect_square(-4, complex=True)
is_perfect_square(-5, complex=True)
is_perfect_square(512j, complex=True)
is_perfect_square(513j, complex=True)
is_perfect_square(1000, complex=True)
