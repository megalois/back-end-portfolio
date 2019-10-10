from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status


class TimestampTests(APITestCase):
    def test_correct_unix_ts(self):
        url = reverse('timestamp-detail', kwargs={'ts': '1450137600'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.data, {'date_ts': 'December 15, 2015', 'unix_ts': 1450137600})

    def test_correct_date_ts(self):
        url = reverse('timestamp-detail', kwargs={'ts': 'December 15, 2015'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.data, {'date_ts': 'December 15, 2015', 'unix_ts': 1450137600})

    def test_incorrect_date(self):
        url = reverse('timestamp-detail', kwargs={'ts': 'LALA'})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
