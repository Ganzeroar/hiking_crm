from rest_framework.generics import ListAPIView
from crm.models import Hikes
from crm.serializers.client.hikes_serializers import HikesSerializer


class AllHikes(ListAPIView):
    queryset = Hikes.objects.all()
    serializer_class = HikesSerializer
