from datetime import datetime


def string_to_date(date: str):
    return datetime.strptime(date, '%d.%m.%Y')
