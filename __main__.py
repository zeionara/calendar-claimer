import os
from datetime import datetime, timedelta

import click

from utils import string_to_date
from .CalendarApiAdapter import CalendarApiAdapter


@click.group()
def main():
    pass


@main.command()
@click.argument('title', type=str)
@click.argument('description', type=str)
@click.argument('name', type=str)
@click.argument('email', type=str)
@click.argument('url', type=str)
@click.argument('source', type=str)
@click.option('--start-date', default=None, type=str)
@click.option('--end-date', default=None, type=str)
@click.option('--start-now', '-sn', is_flag=True)
@click.option('--end-now', '-en', is_flag=True)
@click.option('--offset', '-o', type=int, default=None)
def add_event(title: str, description: str, name: str, email: str, url: str, source: str, start_now: bool, end_now: bool, offset: int = None, start_date: str = None, end_date: str = None):
    assert not (offset is not None and start_now and end_now)
    assert (start_date is None) == (end_date is None)

    if start_date is None and end_date is None:
        day = datetime.now()
        if offset is not None:
            day += timedelta(days=offset)
        CalendarApiAdapter(creds_path=os.environ['GOOGLE_CALENDAR_API_CREDS_PATH']).add_event(
            title=title,
            description=description,
            email=email,
            name=name,
            url=url,
            source=source,
            start_now=start_now,
            end_now=end_now,
            date=day
        )
    else:
        start_date_ = string_to_date(start_date)
        end_date_ = string_to_date(end_date)
        for date in [start_date_ + timedelta(days=i) for i in range((end_date_ - start_date_).days)]:
            CalendarApiAdapter(creds_path=os.environ['GOOGLE_CALENDAR_API_CREDS_PATH']).add_event(
                title=title,
                description=description,
                email=email,
                name=name,
                url=url,
                source=source,
                start_now=start_now,
                end_now=end_now,
                date=date
            )


if __name__ == "__main__":
    main()
