"""A vaccination calculator."""

__author__ = "730324058"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

today: datetime = datetime.today()

one_day: timedelta = timedelta(1)

population: int = int(input("Population: "))
doses_administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_percent: int = int(input("Target percent vaccinated: "))

days_remaining: int = int(round((2/doses_per_day)*((population*(target_percent / 100) - (doses_administered / 2)))))
formatted_days_remaining: timedelta = timedelta(days_remaining)
target_date: datetime = today + formatted_days_remaining
formatted_date: str = target_date.strftime("%B %d, %Y")

print(f"We will reach {target_percent}% vaccination in {days_remaining} days, which falls on {formatted_date}.")