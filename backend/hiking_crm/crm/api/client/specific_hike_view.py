from rest_framework.generics import RetrieveAPIView
from crm.models import Hikes
from crm.serializers.client.hikes_serializer import HikesSerializer


class SpecificHike(RetrieveAPIView):
    queryset = Hikes.objects.all()
    serializer_class = HikesSerializer
