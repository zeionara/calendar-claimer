import os
import pickle
from datetime import datetime

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']


class CalendarApiAdapter:
    def __init__(self, creds_path: str):
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('calendar', 'v3', credentials=creds)

    def add_event(self, title: str, description: str, email: str, name: str, url: str, source: str, start_now: bool = False, end_now: bool = False, date=datetime.now()):
        event = {
            'summary': title,
            'location': 'Saint-Petersburg, Kronverkskiy Prospekt, 49',
            'description': description,
            'start': {
                'dateTime': (date if start_now else datetime.combine(date, datetime.min.time())).isoformat(),
                'timeZone': 'Europe/Moscow',
            },
            'end': {
                'dateTime': (date if end_now else datetime.combine(date, datetime.max.time())).isoformat(),
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

        self.service.events().insert(calendarId=os.environ['CALENDAR_ID'], body=event).execute()
