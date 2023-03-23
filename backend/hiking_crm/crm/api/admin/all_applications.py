from crm.models.applications_for_hike_model import ApplicationsForHike
from crm.serializers.admin.all_applications_serializers import AllApplicationsSerializer
from rest_framework.generics import ListAPIView


class AllApplications(ListAPIView):
    queryset = ApplicationsForHike.objects.all()
    serializer_class = AllApplicationsSerializer
