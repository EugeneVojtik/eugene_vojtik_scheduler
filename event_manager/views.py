from datetime import date
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from event_manager.models import Event, Holidays
from event_manager.serializers import EventSerializer, HolidaySerializer


class CreateEvent(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TodaysEvents(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):
        events = Event.objects.filter(user_id=self.request.user.id)
        today_events = events.filter(event_start__date=date.today())
        return today_events


class ChosenDateEvents(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):
        chosen_date = self.request.POST.__getitem__('date')
        events = Event.objects.filter(user_id=self.request.user.id)
        chosen_date_events = events.filter(event_start__date=chosen_date)
        return chosen_date_events


class MonthEvents(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def get_queryset(self):

        events = Event.objects.filter(
            user_id=self.request.user.id,
            event_start__month=date.today().month
        )
        return events


class UsersHolidays(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = HolidaySerializer
    queryset = Holidays.objects.all()

    def get_queryset(self):
        your_holidays = Holidays.objects.filter(
            country=self.request.user.country_id
        )
        return your_holidays
