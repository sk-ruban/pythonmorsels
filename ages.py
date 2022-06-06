from datetime import datetime, timedelta


def is_over(limit, birthday):
    birthday_formatted = datetime.fromisoformat(birthday)

    if birthday_formatted + timedelta(days=limit*365) < datetime.today():
        return True
    else:
        return False


is_over(18, '1982-03-15')