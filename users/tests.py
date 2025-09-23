from rest_framework.test import APITestCase
from rest_framework import status

from users.models import CustomUser


# Create your tests here.
class TestRegister(APITestCase):

    def test_create_user(self):
        data = {
            'username': 'admin',
            'email': 'admin@gmail.com',
            'password1': 'admin',
            'password2': 'admin',
        }
        response = self.client.post('/users/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestLogin(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='admin', email='admin@gmail.com', password='admin', )

    def test_login(self):
        data = {
            'email': 'admin@gmail.com',
            'password': 'admin',
        }
        response = self.client.post('/users/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestLogout(APITestCase):

    def setUp(self):
        self.user = CustomUser.objects.create_user(username='admin', email='admin@gmail.com', password='admin', )
        self.client.force_authenticate(self.user)

    def test_logout(self):
        response = self.client.post('/users/logout/', )
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestUser(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username='admin', email='admin@gmail.com', password='admin', pk=1)
        self.client.force_authenticate(self.user)

    def test_retrieve(self):
        response = self.client.get('/users/detail/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        data = {
            'username': 'admin1',
            'email': 'admin@gmail.com',
            'password1': 'admin',
            'password2': 'admin',
        }
        response = self.client.put('/users/update/1', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        response = self.client.delete('/users/delete/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list(self):
        response = self.client.get('/users/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
