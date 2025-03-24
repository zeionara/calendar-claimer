# Calendar claimer

## Usage guide

1. Clone the repo to your home directory

```sh
git clone https://github.com/zeionara/calendar-claimer.git /home/$USER/calendar-claimer
```

2. Install dependencies

```
pip install click google-api-python-client google-auth-oauthlib
```

3. Configure your shell profile

```
export GOOGLE_CALENDAR_API_CREDS_PATH=/home/$USER/.creds/key.json
export CALENDAR_ID=primary

ac () {
  cd /home/$USER/calendar-claimer
  conda run -n calendar-claimer python -m cc add-event $1 $2 $3
}
```

4. Generate API key from [google console](https://console.cloud.google.com/apis) with [enabled calendar API](https://console.cloud.google.com/apis/api/calendar-json.googleapis.com) and save it as `/home/$USER/.creds/key.json`

5. Enjoy (here `foo` is the event title, `08:00` is the start time, then first `/-1` means that event starts yesterday, `09:00` is the end time, then second `/-1` means that event ends yesterday)

```
ac foo 08:00/-1 09:00/-1
```
