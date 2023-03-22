from crm.models.applications_for_hike_model import ApplicationsForHike
from django.urls import reverse
from rest_framework.test import APITestCase


class AllApplicationsTest(APITestCase):

    def test_return_all_hikes(self):
        url = reverse('applications')
        response = self.client.get(url)

        self.assertEqual(len(response.data), ApplicationsForHike.objects.count())
