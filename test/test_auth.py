import requests
from django.test import Client


class TestClass(object):

    def test_get_login(self):
        response = requests.get('http://localhost:8000/')
        assert response.status_code == 200
