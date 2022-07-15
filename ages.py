from datetime import datetime

'''
from dateutil.relativedelta import relativedelta

# Unable to use relativedelta as PythonMorsels does not accept dateutil

def is_over(limit, birthday):

    """Return True if person is above a certain age"""
    
    birthday_formatted = datetime.fromisoformat(birthday)
    today = datetime(3000,2,28)
    if birthday_formatted + relativedelta(years=limit) < today:
        return True
    else:
        return False
'''


def is_over(limit, birthday):

    """Return True if person is above a certain age"""

    birthday_formatted = datetime.fromisoformat(birthday)
    today = datetime(2016, 2, 29)
    if birthday_formatted.year + limit > today.year:
        return False
    elif birthday_formatted.year + limit == today.year:
        if birthday_formatted.month > today.month:
            return False
        elif birthday_formatted.month == today.month:
            if birthday_formatted.day > today.day:
                return False
            else:
                return True
        else:
            return True
    else:
        return True


def get_age(birthday, exact=False):

    """Return a person's current age given their birthdate"""

    counter = 0
    for age in range(1, 1000):
        if is_over(age, birthday):
            counter = age
    print(counter)


# Base Problem
is_over(18, '2982-03-15')
is_over(18, '2982-02-15')
is_over(18, '2990-04-15')

# Bonus 1
is_over(16, '2984-02-29')
is_over(16, '2984-02-27')
is_over(16, '2984-03-01')

# Bonus 2
get_age('1942-01-08')
get_age('1815-02-28')
get_age('2980-02-28')
get_age('2980-08-28')

# Bonus 3
get_age('2984-02-29', exact=True)
float(get_age('2984-02-29', exact=True))
float(get_age('2984-02-27', exact=True))