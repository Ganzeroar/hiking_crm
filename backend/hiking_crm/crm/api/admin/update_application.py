from crm.models.applications_for_hike_model import ApplicationsForHike
from crm.serializers.admin.all_applications_serializer import AllApplicationsSerializer
from rest_framework.generics import UpdateAPIView


class UpdateApplication(UpdateAPIView):
    queryset = ApplicationsForHike.objects.all()
    serializer_class = AllApplicationsSerializer
