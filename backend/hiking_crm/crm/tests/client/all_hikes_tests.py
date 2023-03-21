from crm.models.hikes_model import Hikes
from django.urls import reverse
from rest_framework.test import APITestCase


class AllHikesTest(APITestCase):

    def test_return_all_hikes(self):
        url = reverse('client-hikings')
        response = self.client.get(url)

        self.assertEqual(len(response.data), Hikes.objects.count())
