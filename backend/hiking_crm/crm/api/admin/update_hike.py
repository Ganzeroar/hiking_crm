from crm.models.hikes_model import Hikes
from crm.serializers.admin.admin_hikes_serializers import AdminSpecificHikesSerializer
from rest_framework.generics import UpdateAPIView


class UpdateHike(UpdateAPIView):
    queryset = Hikes.objects.all()
    serializer_class = AdminSpecificHikesSerializer
