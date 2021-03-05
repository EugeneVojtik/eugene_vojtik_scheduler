from django.core.management import BaseCommand
from requests import get
from ics import Calendar

from event_manager.models import Country, Holidays


class Command(BaseCommand):
    def handle(self, *args, **options):
        countries = Country.objects.all()
        holidays_names_list = []

        for country in countries:
            try:
                url = f"https://www.officeholidays.com/ics-clean/" + country.country_name
                holidays = Calendar(get(url).text)
                for holiday in holidays.events:
                    if holiday.name not in holidays_names_list:
                        Holidays.objects.create(
                            country_id=country.id,
                            holiday=holiday.name,
                            holiday_start=holiday._begin.date(),
                            holiday_finish=holiday._end_time.date()
                        )
                        holidays_names_list.append(holiday.name)
            except Exception:
                print(country.country_name)
                continue
