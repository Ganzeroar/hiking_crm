from rest_framework.generics import ListAPIView
from crm.models import Hikes
from crm.serializers.admin.admin_hikes_serializers import AdminHikesSerializer


class AdminAllHikes(ListAPIView):
    queryset = Hikes.objects.all()
    serializer_class = AdminHikesSerializer
