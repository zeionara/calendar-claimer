# Installation
```
conda env create -f calendar-claimer/environment.yml
export GOOGLE_CALENDAR_API_CREDS_PATH=key.json
export CALENDAR_ID=primary
```
# Usage
```
python -m calendar-claimer add-event -sn "Hello world!" "Test event" "Zeio Nara" zeionara@gmail.com http://github.com/zeionara github
```
