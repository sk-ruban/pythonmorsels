import datetime
from datetime import date


class NextDate:

    def __init__(self, day, *, after_today=False):
        self.day = day
        self.after_today = after_today

    def days_until(self):
        if self.after_today:
            print(self.day - date.today().weekday() % 7 if 0 else 7)
            return self.day - date.today().weekday() % 7 if 0 else 7
        else:
            print((self.day - date.today().weekday()) % 7)
            return (self.day - date.today().weekday()) % 7

    def date(self):
        if self.after_today:
            print(date.today() + datetime.timedelta(self.days_until()))
            return date.today() + datetime.timedelta(self.days_until())
        else:
            print(date.today() + datetime.timedelta(self.days_until()))
            return date.today() + datetime.timedelta(self.days_until())

    def __repr__(self):
        if self.after_today:
            return f"NextDate(Weekday.{self.day}2)"
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


# print(date.today())
next_thursday = NextDate(Weekday.THURSDAY)
next_thursday.days_until()
next_thursday.date()
next_friday = NextDate(Weekday.FRIDAY)
next_friday.days_until()
next_friday.date()
next_friday = NextDate(Weekday.THURSDAY, after_today=True)
next_friday.days_until()
next_friday.date()

