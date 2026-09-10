from datetime import datetime


def today_date():
    current = datetime.now()
    return current.strftime("%Y-%m-%d")


def change_date_format(value):
    try:
        date = datetime.strptime(value, "%Y-%m-%d")
        return date.strftime("%d-%m-%Y")
    except ValueError:
        return "Invalid date format!"


def days_between(first_date, second_date):
    try:
        first = datetime.strptime(first_date, "%Y-%m-%d")
        second = datetime.strptime(second_date, "%Y-%m-%d")
        difference = second - first
        return abs(difference.days)
    except ValueError:
        return "Invalid date format!"
