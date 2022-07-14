from datetime import datetime
from dateutil.relativedelta import relativedelta


# def is_over(limit, birthday):
#     birthday_formatted = datetime.fromisoformat(birthday)
#     today = datetime(3000,2,28)
#     if birthday_formatted + relativedelta(years=limit) < today:
#         print(birthday_formatted.replace(year=birthday_formatted.year + limit))
#         print(birthday_formatted + relativedelta(years=limit))
#         print("True")
#         return True
#     else:
#         print(birthday_formatted + relativedelta(years=limit))
#         print("False")
#         return False

def is_over(limit, birthday):

    # Return True if person is above a certain age

    birthday_formatted = datetime.fromisoformat(birthday)
    today = datetime(2000, 3, 16)
    if birthday_formatted.year + limit > today.year:
        print("False1")
    elif birthday_formatted.year + limit == today.year:
        if birthday_formatted.month > today.month:
            print("False2")
        elif birthday_formatted.month == today.month:
            if birthday_formatted.day > today.day:
                print("False3")
            else:
                print("True")
        else:
            print("True")
    else:
        print("True")
    

# Base Problem
is_over(18, '2982-03-15')
is_over(18, '2982-02-15')
is_over(18, '2990-04-15')

# Bonus 1
is_over(16, '2984-02-29')
is_over(16, '2984-02-27')
is_over(16, '2984-03-01')