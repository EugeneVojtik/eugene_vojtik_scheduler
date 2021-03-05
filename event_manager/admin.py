from django.contrib import admin

# Register your models here.
from event_manager.models import SchedulerUser, Event, Holidays

admin.site.register(SchedulerUser)
admin.site.register(Event)
admin.site.register(Holidays)