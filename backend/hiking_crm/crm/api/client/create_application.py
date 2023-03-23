from crm.models.applications_for_hike_model import ApplicationsForHike
from crm.serializers.client.application_serializers import ApplicationSerializer
from rest_framework.generics import CreateAPIView


class CreateApplication(CreateAPIView):
    queryset = ApplicationsForHike.objects.all()
    serializer_class = ApplicationSerializer
