import datetime

from rest_framework.test import APITestCase
from rest_framework import status

from telegram_bot.models import Habit, PleasantHabit
from users.models import CustomUser


# Create your tests here.
class TestHabit(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='admin', email='admin@gmail.com', password='admin')
        self.client.force_authenticate(self.user)
        self.habit = Habit.objects.create(name='test', place='fas', time=datetime.datetime.now(), action_do='plak', time_do='100', is_public=True, award='fad', period_days=2, owner=self.user, pk=3)
        print(self.habit)

    def test_create_habit(self):
        data = {
            "name": "admin",
            "place": "fdsa",
            "time": "2021-01-12T12:00:00",
            "action_do": "plak",
            "time_do": "100",
            "is_public" : False,
            'award': 'fdsafa',
            'period_days': 2,
        }
        response = self.client.post('/habit/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_habit(self):
        response = self.client.get('/habit/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_habit(self):
        response = self.client.delete('/habit/delete/3')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_habit(self):
        response = self.client.get('/habit/3')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habit(self):
        data = {
            "name": "admin",
            "place": "fdsa",
            "time": "2021-01-12T12:00:00",
            "action_do": "plak",
            "time_do": "100",
            "is_public": False,
            'award': 'fdsafa',
            'period_days': 2,
        }
        response = self.client.put('/habit/update/3', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestPleasantHabit(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='admin', email='admin@gmail.com', password='admin')
        self.client.force_authenticate(self.user)
        self.habit = PleasantHabit.objects.create(name='test', action_do='plak', is_public=True, owner=self.user,
                                          pk=3)

    def test_create_pleasant_habit(self):
        data = {
            "name": "admin",
            "action_do": "plak",
            "is_public": False,
        }
        response = self.client.post('/habit/pleasant_habit/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_pleasant_habit(self):
        response = self.client.get('/habit/pleasant_habit/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_pleasant_habit(self):
        response = self.client.get('/habit/pleasant_habit/3')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_pleasant_habit(self):
        data = {
            "name": "test",
            "action_do": "plak",
            "is_public": False,
        }
        response = self.client.put('/habit/pleasant_habit/update/3', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_pleasant_habit(self):
        response = self.client.delete('/habit/pleasant_habit/delete/3')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_value_validation(self):
        data = {
            "name": "admin",
            "place": "fdsa",
            "time": "2021-01-12T12:00:00",
            "action_do": "plak",
            "time_do": "100",
            "is_public": False,
            'award': 'fdsafa',
            'connected_habit': 3,
            'period_days': 2,
        }
        response = self.client.post('/habit/create/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_period_validation(self):
        data = {
            "name": "admin",
            "place": "fdsa",
            "time": "2021-01-12T12:00:00",
            "action_do": "plak",
            "time_do": "100",
            "is_public": False,
            'award': 'fdsafa',
            'period_days': 8,
        }
        response = self.client.post('/habit/create/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_time_validation(self):
        data = {
            "name": "admin",
            "place": "fdsa",
            "time": "2021-01-12T12:00:00",
            "action_do": "plak",
            "time_do": "121",
            "is_public": False,
            'award': 'fdsafa',
            'period_days': 2,
        }
        response = self.client.post('/habit/create/', data)
