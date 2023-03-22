from rest_framework.generics import RetrieveAPIView
from crm.models import Hikes
from crm.serializers.admin.admin_hikes_serializers import AdminSpecificHikesSerializer


class AdminSpecificHike(RetrieveAPIView):
    queryset = Hikes.objects.all()
    serializer_class = AdminSpecificHikesSerializer
