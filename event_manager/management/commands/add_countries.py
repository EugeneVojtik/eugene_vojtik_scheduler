import requests
from django.core.management import BaseCommand
from bs4 import BeautifulSoup


from event_manager.models import Country


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = "https://www.officeholidays.com/countries/"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, features='html.parser')
        countries_list = [
            country['href'].removeprefix(url)
            for country in soup.find_all('a', href=True)
            if '/countries/' in country['href']
        ]
        for country in countries_list:
            Country.objects.create(country_name=country)
        Country.objects.first().delete()  # first element is deleted manually as it is not a Country
