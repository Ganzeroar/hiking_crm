from crm.models.applications_for_hike_model import ApplicationsForHike
from crm.models.statuses_model import Statuses
from django.urls import reverse
from rest_framework.test import APITestCase


class UpdateApplicationTest(APITestCase):

    def test_update_application(self):
        application = ApplicationsForHike.objects.first()

        url = reverse('update-application', kwargs={'pk': application.id})

        current_status = application.status

        new_status_id = 2 if current_status.id == 1 else 1

        new_status = Statuses.objects.get(id=new_status_id)

        data = {
            'id': application.id,
            'client': {
                'id': application.client.id,
                'client_name': application.client.client_name,
                'client_email': application.client.client_email,
                'client_phone': str(application.client.client_phone),
            },
            'hike': {
                'id': application.hike.id,
                'hike_name': application.hike.hike_name,
            },
            'status': {
                'id': new_status.id,
                'status_name': new_status.status_name,
            },
            'date_of_creation': application.date_of_creation,
        }

        self.client.put(url, data=data, format='json')

        application_after_update = ApplicationsForHike.objects.first()

        self.assertEqual(application_after_update.status.id, new_status.id)
