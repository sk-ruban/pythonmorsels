import datetime
from datetime import date


class NextDate:

    """Answers questions about the next Monday/Tuesday/etc."""

    def __init__(self, day, *, after_today=False):
        self.day = day
        self.after_today = after_today

    def days_until(self):
        # Calculates the days difference mod 7
        days_difference = (self.day - date.today().weekday()) % 7
        if self.after_today & (days_difference == 0):
            return 7
        else:
            return days_difference

    def date(self):
        return date.today() + datetime.timedelta(self.days_until())

    def __repr__(self):
        if self.after_today:
            return f"NextDate(Weekday.{self.day}, after_today=True)"
        else:
            return f"NextDate(Weekday.{self.day})"


class Weekday:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def next_date(day, after_today=False):
    return date.today() + datetime.timedelta(days_until(day, after_today))


def days_until(day, after_today=False):
    days_difference = (day - date.today().weekday()) % 7
    if after_today & (days_difference == 0):
        return 7
    else:
        return days_difference


def next_tuesday(after_today=False):
    return next_date(Weekday.TUESDAY, after_today)


def days_to_tuesday(after_today=False):
    return days_until(Weekday.TUESDAY, after_today)


next_thursday = NextDate(Weekday.THURSDAY)
next_thursday.days_until()
next_thursday.date()
next_friday = NextDate(Weekday.FRIDAY)
next_friday.days_until()
next_friday.date()
next_friday = NextDate(Weekday.THURSDAY, after_today=True)
next_friday.days_until()
next_friday.date()

# Bonus 3
next_date(Weekday.FRIDAY)
days_until(Weekday.FRIDAY)
next_tuesday(after_today=True)
days_to_tuesday()



