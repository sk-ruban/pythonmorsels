import decimal
from decimal import Decimal


def is_perfect_square(num):
    if type(num) is not str:
        if num > 0:
            with decimal.localcontext() as c:
                c.prec = 2000
            num = Decimal(num)
            print(num.sqrt() % 1 == 0)
            return num.sqrt() % 1 == 0
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
is_perfect_square(10**2000 - 1)
print(Decimal(10**2000 % 1).sqrt())

print(decimal.getcontext().prec)