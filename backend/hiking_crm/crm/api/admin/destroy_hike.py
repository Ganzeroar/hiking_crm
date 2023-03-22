from crm.models.hikes_model import Hikes
from crm.serializers.admin.admin_hikes_serializers import AdminSpecificHikesSerializer
from rest_framework.generics import DestroyAPIView


class DestroyHike(DestroyAPIView):
    queryset = Hikes.objects.all()
    serializer_class = AdminSpecificHikesSerializer
