import os
from datetime import datetime, timedelta

import click

from .utils import string_to_date, string_to_datetime
from .CalendarApiAdapter import CalendarApiAdapter


@click.group()
def main():
    pass


@main.command()
@click.argument('title', type=str)
@click.argument('start', type = str)
@click.argument('end', type = str)
@click.option('--description', default = None, type=str)
@click.option('--name', default = None, type=str)
@click.option('--email', default = None, type=str)
@click.option('--url', default = None, type=str)
@click.option('--source', default = None, type=str)
def add_event(title: str, start: str, end: str, description: str, name: str, email: str, url: str, source: str):
    # assert not (offset is not None and start_now and end_now)
    # assert (start_date is None) == (end_date is None)

    start = string_to_datetime(start)
    end = string_to_datetime(end)

    if end < start:
        raise ValueError('End time is earlier than start time')

    CalendarApiAdapter(creds_path=os.environ['GOOGLE_CALENDAR_API_CREDS_PATH']).add_event(
        title=title,
        description=description,
        email=email,
        name=name,
        url=url,
        source=source,
        start = start,
        end = end
    )


if __name__ == "__main__":
    main()
