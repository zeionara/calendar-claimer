from datetime import datetime, timedelta


def string_to_date(date: str):
    return datetime.strptime(date, '%d.%m.%Y')


def string_to_datetime(date: str):
    date_components = date.split('/')

    if len(date_components) > 1:
        date_increment = int(date_components[1])
    else:
        date_increment = 0

    date = datetime.now() + timedelta(days = date_increment)
    time = datetime.strptime(date_components[0], '%H:%M').time()

    return datetime.combine(date, time)
