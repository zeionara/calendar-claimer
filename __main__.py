import os
from datetime import datetime

import click

from CalendarApiAdapter import CalendarApiAdapter


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
@click.option('--start-now', '-sn', is_flag=True)
@click.option('--end-now', '-en', is_flag=True)
def add_event(title: str, description: str, name: str, email: str, url: str, source: str, start_now: bool, end_now: bool):
    adapter = CalendarApiAdapter(creds_path=os.environ['GOOGLE_CALENDAR_API_CREDS_PATH'])

    event = {
        'summary': title,
        'location': 'Saint-Petersburg, Kronverkskiy Prospekt, 49',
        'description': description,
        'start': {
            'dateTime': (datetime.now() if start_now else datetime.combine(datetime.today(), datetime.min.time())).isoformat(),
            'timeZone': 'Europe/Moscow',
        },
        'end': {
            'dateTime': (datetime.now() if end_now else datetime.combine(datetime.today(), datetime.max.time())).isoformat(),
            'timeZone': 'Europe/Moscow',
        },
        'attendees': [
            {
                'email': email,
                'responseStatus': 'accepted',
                'displayName': name
            }
        ],
        'source': {
            'url': url,
            'title': source
        },
        'reminders': {
            'useDefault': False
        }
    }
    event = adapter.service.events().insert(calendarId=os.environ['CALENDAR_ID'], body=event).execute()


if __name__ == "__main__":
    main()
