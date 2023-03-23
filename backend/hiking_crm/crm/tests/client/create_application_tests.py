from crm.models.applications_for_hike_model import ApplicationsForHike
from crm.models.clients_model import Clients
from crm.models.hikes_model import Hikes
from django.urls import reverse
from rest_framework.test import APITestCase


class CreateApplicationTest(APITestCase):

    def test_create_application(self):
        number_of_applications_before_request = ApplicationsForHike.objects.count()

        url = reverse('create-application')
        hike = Hikes.objects.first()
        data = {
            'client': {
                'client_name': 'name1',
                'client_email': 'email2@qwe.com',
                'client_phone': '+79823212883',
            },
            'hike': {
                'id': hike.id,
            },
        }
        response = self.client.post(url, data=data, format='json')
        number_of_applications_after_request = ApplicationsForHike.objects.count()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(number_of_applications_before_request + 1, number_of_applications_after_request)

    def test_create_new_client_if_not_exist(self):
        number_of_clients_before_request = Clients.objects.count()

        url = reverse('create-application')
        hike = Hikes.objects.first()

        data = {
            'client': {
                'client_name': 'name1',
                'client_email': 'email2@qwe.com',
                'client_phone': '+79823212883',
            },
            'hike': {
                'id': hike.id,
            },
        }
        response = self.client.post(url, data=data, format='json')

        number_of_clients_after_request = Clients.objects.count()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(number_of_clients_before_request + 1, number_of_clients_after_request)

    def test_doesnt_create_new_client_if_exist(self):
        number_of_clients_before_request = Clients.objects.count()

        client = Clients.objects.first()

        url = reverse('create-application')
        hike = Hikes.objects.first()
        data = {
            'client': {
                'client_name': client.client_name,
                'client_email': client.client_email,
                'client_phone': str(client.client_phone),
            },
            'hike': {
                'id': hike.id,
            },
        }
        response = self.client.post(url, data=data, format='json')

        number_of_clients_after_request = Clients.objects.count()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(number_of_clients_before_request, number_of_clients_after_request)

    def test_return_error_if_hike_id_is_not_valid(self):
        url = reverse('create-application')
        data = {
            'client': {
                'client_name': 'name1',
                'client_email': 'email2@qwe.com',
                'client_phone': '+79823212883',
            },
            'hike': {
                'id': 'qwe',
            },
        }
        response = self.client.post(url, data=data, format='json')

        response_data = response.data.get('hike').get('id')[0]

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data, 'A valid integer is required.')

    def test_return_error_if_client_data_is_not_valid(self):
        url = reverse('create-application')
        hike = Hikes.objects.first()

        data = {
            'client': {
                'client_name': 'name',
                'client_email': 'email2@@@@@qwe.com',
                'client_phone': '+79823212883',
            },
            'hike': {
                'id': hike.id,
            },
        }
        response = self.client.post(url, data=data, format='json')

        response_data = response.data.get('client').get('client_email')[0]

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data, 'Enter a valid email address.')
