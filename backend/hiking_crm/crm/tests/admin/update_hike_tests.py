from crm.models.hikes_model import Hikes
from django.urls import reverse
from rest_framework.test import APITestCase


class UpdateHikeTest(APITestCase):

    def test_update_hike(self):
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

    def test_update_hike_return_error_if_name_invalid(self):
        hike = Hikes.objects.first()
        url = reverse('update-hike', kwargs={'pk': hike.id})

        new_hike_name = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

        data = {
            'id': 'hike.id',
            'hike_name': new_hike_name,
            'hike_description': hike.hike_description,
        }

        response = self.client.put(url, data=data, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.get('hike_name')[0], 'Ensure this field has no more than 100 characters.')

    def test_update_application_return_error_if_description_invalid(self):
        hike = Hikes.objects.first()
        url = reverse('update-hike', kwargs={'pk': hike.id})

        new_hike_description = """
            Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        """ * 4

        data = {
            'id': 'hike.id',
            'hike_name': hike.hike_name,
            'hike_description': new_hike_description,
        }

        response = self.client.put(url, data=data, format='json')

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.get('hike_description')[0], 'Ensure this field has no more than 2000 characters.')
