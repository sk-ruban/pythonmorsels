import datetime
from datetime import date


class NextDate:

    def __init__(self, day):
        self.day = day

    def days_until(self):
        print((self.day - date.today().weekday()) % 7)
        return (self.day - date.today().weekday()) % 7

    def date(self):
        print(date.today() + datetime.timedelta(self.days_until()))
        return date.today() + datetime.timedelta(self.days_until())

    def __repr__(self):
        return f"NextDate(Weekday.{self.day})"


class Weekday:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


print(date.today())
print(date(1999, 12, 31))
next_thursday = NextDate(Weekday.THURSDAY)
next_thursday.days_until()
next_thursday.date()

