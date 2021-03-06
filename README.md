"# EugeneVojtik_scheduler" 

This is Django application for scheduling events and have reminders for it.

In order to test this application you can use temporary email by using the link below:
https://temp-mail.org/

Import modules setup for testing of application:
```bash
from requests import post, get
from datetime import timedelta, datetime
```

To get register please kindly use code below and input your email/password/username data to blank fiels: 
```bash
data = {
    "username": "__username__",
    "email": "__email__",
    "password": "__password__",
    "country": "__country_code__"
}
response = post("https://scheduler-reminder-app.herokuapp.com/auth/register", data=data)

```
Login:
```bash
data = {
    'email': '___your_email___',
    'password': '__password__'
}
response = post('https://scheduler-reminder-app.herokuapp.com/event/login', data=data)
response
```

For getting token sent to your email please use code below
Make sure you have input correct data in blank fields.
```bash
data = {
    "email": "_____________",
    "password": "______"
}
response = post('https://scheduler-reminder-app.herokuapp.com/auth/create_token', data=data)

```
Please use code below for adding event.
Please note there are few options for reminding of upcoming event:

> 1. timedelta(seconds=3600) -  in 1h
> 2. timedelta(seconds=7200) - in 2h
> 3. timedelta(seconds=14400) - in 4h
> 4. timedelta(seconds=86400) - day before
> 5. timedelta(seconds=604800) - week before
> 
```bash
headers = {'Authorization': 'Token ______your_token__________'}
data = {
    'event': f'___event_name____',
    'event_start': f'YYYY-MM-DD HH:MM:SS',
    'remind_option' : __reminder_option__,
}
response = post('https://scheduler-reminder-app.herokuapp.com/event/create_event', headers=headers, data=data)
 ```
Get your events in a month period:
```BASH
headers = {"Authorization": "Token ___your_token___"}
response = get("https://scheduler-reminder-app.herokuapp.com/event/month_events", headers=headers)
response.json()
```

Get your holidays list
```BASH
headers={'Authorization': "Token ___your_token___"}
response = get("https://scheduler-reminder-app.herokuapp.com/event/holidays", headers=headers)
response.json()
```
Events that you have today:
```bash
headers = {'Authorization': 'Token ___your_token___'}
response = get('https://scheduler-reminder-app.herokuapp.com/event/todays_events', headers=headers)
response.json()
```
If you have a particular date to check if you have scheduled events please execute below code: 
```bash
headers = {'Authorization': 'Token 3480be8df73788d206f1cd4c624914aaedf9450d'}
data = {"date": 'YYYY-MM-DD'}
response = get("https://scheduler-reminder-app.herokuapp.com/event/date_events", headers=headers, data=data)
response.json()
```

