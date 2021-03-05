from django.db import models
from django.contrib.auth.models import AbstractUser

from scheduler_APP.settings import REMIND_OPTIONS


class Event(models.Model):
    event = models.TextField(max_length=2000, verbose_name='Your event', null=True)
    user = models.ForeignKey('SchedulerUser', on_delete=models.CASCADE, related_name='user_event', null=True)
    event_start = models.DateTimeField(null=True)
    event_finish = models.DateTimeField(null=True, blank=True)
    remind_option = models.CharField(max_length=30, choices=REMIND_OPTIONS, null=True, blank=True)
    time_to_remind = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.event

    def save(self, **kwargs):
        if self.event_finish is None:
            self.event_finish = self.event_start
        if self.remind_option:
            self.time_to_remind = self.event_start - self.remind_option

        super().save(**kwargs)


class Country(models.Model):
    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'

    country_name = models.TextField()

    def __str__(self):
        return self.country_name


class SchedulerUser(AbstractUser):
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True,
        blank=True, related_name='country_user',
        verbose_name='Country'
    )
    USERNAME_FIELD = 'email'
    email = models.EmailField(unique=True, blank=False)
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class Holidays(models.Model):
    class Meta:
        verbose_name = 'holiday'
        verbose_name_plural = 'holidays'

    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, null=True,
        blank=True, related_name='country_holiday',
    )
    holiday = models.TextField(null=True)
    holiday_start = models.DateField(null=True)
    holiday_finish = models.DateField(null=True)

    def __str__(self):
        return self.holiday
