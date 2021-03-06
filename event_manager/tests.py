# Create your tests here.
from json import dumps
from rest_framework.authtoken.models import Token
from django.urls import reverse
from rest_framework import status
from rest_framework.test import RequestsClient, APITestCase

from event_manager.models import SchedulerUser


class RestTest(APITestCase):
    def setUp(self):
        self.login = "test_login"
        self.email = 'test@mail.com'
        self.password = "testtest"
        self.user = SchedulerUser.objects.create_user(
            username=self.login,
            password=self.password,
            email=self.email
        )

    

    def test_get_event(self):
        url = reverse("create_token")
        data = {
            "login": self.login,
            "email": self.email,
            "password": self.password
        }
        response = self.client.post(
            path=url,
            data=dumps(data),
            content_type="application/json"
        )
        client = RequestsClient()
        headers = {'Authorization': 'Token ' + Token.objects.get(user=self.user).key}
        response = client.get('http://127.0.0.1:8000/event/create_event', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_event(self):
        url = reverse("create_token")
        data = {
            "login": self.login,
            "email": self.email,
            "password": self.password
        }
        response = self.client.post(
            path=url,
            data=dumps(data),
            content_type="application/json"
        )
        client = RequestsClient()

        headers = {'Authorization': 'Token ' + Token.objects.get(user=self.user).key}
        data = {
            "event": 'test_test',
            "event_start": '2021-03-06 18:00:00',

        }
        response = client.post('http://127.0.0.1:8000/event/create_event', headers=headers, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_holidays(self):
        url = reverse("create_token")
        data = {
            "login": self.login,
            "email": self.email,
            "password": self.password
        }
        response = self.client.post(
            path=url,
            data=dumps(data),
            content_type="application/json"
        )
        client = RequestsClient()
        headers = {'Authorization': 'Token ' + Token.objects.get(user=self.user).key}
        response = client.get('http://127.0.0.1:8000/event/holidays', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
