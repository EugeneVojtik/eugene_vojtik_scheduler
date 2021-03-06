from event_manager.models import Event
from datetime import datetime, timedelta
from celery import shared_task
from django.core.mail import send_mail
import pytz
from scheduler_APP.settings import EMAIL_HOST_USER


@shared_task()
def to_remind():
    events_set = Event.objects.filter(remind_option__isnull=False)
    for event in events_set:
        current_time = pytz.UTC.localize(datetime.now() + timedelta(hours=3))
        if event.time_to_remind <= current_time:
            subject = 'Upcoming event notification'
            message = f'Please be informed of upcoming event, details are below: \n' \
                      f'Event: {event.event} \n Event starts: {event.event_start} and ends ' \
                      f'{event.event_finish}'
            send_mail(
                subject=subject,
                message=message,
                from_email=EMAIL_HOST_USER,
                recipient_list=[event.user.email]
            )
            Event.objects.filter(id=event.id).update(remind_option=None)
