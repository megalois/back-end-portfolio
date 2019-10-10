from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory


class HeaderParserTests(APITestCase):
    def test_returns_user_agent(self):
        url = reverse('header-parser-detail')
        factory = APIRequestFactory()
        request = factory.get(url, HTTP_USER_AGENT='Mozilla/5.0')
        response = self.client.get(url, HTTP_USER_AGENT='Mozilla/5.0', format='json')
        self.assertEqual(response.data, request.META['HTTP_USER_AGENT'])

