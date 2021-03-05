from django.urls import path

from event_manager.views import UsersHolidays, CreateEvent, MonthEvents, TodaysEvents, ChosenDateEvents

urlpatterns = [
    path('holidays', UsersHolidays.as_view(), name='users_holidays'),
    path('create_event', CreateEvent.as_view(), name='create_event'),
    path('todays_events', TodaysEvents.as_view(), name='todays_event'),
    path('date_events', ChosenDateEvents.as_view(), name='date_events'),
    path('month_events', MonthEvents.as_view(), name='month_events'),
]