from crm.models.hikes_model import Hikes
from django.urls import reverse
from rest_framework.test import APITestCase


class DestroyHikeTest(APITestCase):

    def test_destroy_hike(self):
        hike = Hikes.objects.first()
        url = reverse('destroy-hike', kwargs={'pk': hike.id})
        hikes_count = Hikes.objects.count()

        self.client.delete(url)

        hikes_count_after_destroy = Hikes.objects.count()

        self.assertEqual(hikes_count - 1, hikes_count_after_destroy)
