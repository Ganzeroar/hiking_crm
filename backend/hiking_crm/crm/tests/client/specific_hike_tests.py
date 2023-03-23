from crm.models.hikes_model import Hikes
from django.urls import reverse
from rest_framework.test import APITestCase


class SpecificHikesTest(APITestCase):

    def test_return_specific_hike(self):
        hike_pk = 2
        url = reverse('specific-hike', kwargs={'pk': hike_pk})
        response = self.client.get(url)

        hike = Hikes.objects.get(pk=hike_pk)

        self.assertEqual(response.data.get('id'), hike.pk)
        self.assertEqual(response.data.get('hike_name'), hike.hike_name)
        self.assertEqual(response.data.get('hike_description'), hike.hike_description)
