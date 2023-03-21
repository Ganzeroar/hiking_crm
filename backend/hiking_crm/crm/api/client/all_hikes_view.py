from rest_framework import generics
from crm.models import Hikes
from crm.serializers.client.hikes_serializer import HikesSerializer


class AllHikes(generics.ListAPIView):
    queryset = Hikes.objects.all()
    serializer_class = HikesSerializer
