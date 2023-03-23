from crm.models.hikes_model import Hikes
from django.urls import reverse
from rest_framework.test import APITestCase


class UpdateHikeTest(APITestCase):

    def test_update_application(self):
        hike = Hikes.objects.first()
        url = reverse('update-hike', kwargs={'pk': hike.id})

        new_hike_name = 'Новый поход'

        data = {
            'id': hike.id,
            'hike_name': new_hike_name,
            'hike_description': hike.hike_description,
        }

        self.client.put(url, data=data, format='json')

        hike_after_update = Hikes.objects.first()

        self.assertEqual(hike_after_update.hike_name, new_hike_name)
