from rest_framework.serializers import ModelSerializer
from event_manager.models import Event, Holidays


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ('event', 'event_start', 'event_finish', 'remind_option',)


class HolidaySerializer(ModelSerializer):
    class Meta:
        model = Holidays
        fields = ('holiday', 'holiday_start', 'holiday_finish',)


class MonthSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_start', 'event']
