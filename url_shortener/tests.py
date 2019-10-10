import json
from django.core.exceptions import ValidationError
from django.urls import reverse
from rest_framework import serializers
from rest_framework import status
from rest_framework.test import APITestCase
from url_shortener.models import URL
from url_shortener.shortener import ShortURL


def create_url(url):
    return URL.objects.create(url=url)


class URLTests(APITestCase):
    def test_list_urls(self):
        url = reverse('url-list')
        create_url(url='https://github.com')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        d = {"id": 1, "url": 'https://github.com'}
        self.assertEqual(response.json(), [d])

    def test_post_correct_url(self):
        url = reverse('url-list')
        data = {'url': 'http://lala.com'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_incorrect_url(self):
        url = reverse('url-list')
        data = {'url': 'fsafljsh'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_using_the_shortened_url(self):
        shortener = ShortURL()
        url_obj = create_url('http://lala.com')
        url = reverse('url-detail', kwargs={'short_url': shortener.encode(url_obj.id)})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
