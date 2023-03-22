from crm.models import ApplicationsForHike
from crm.serializers.admin.clients_serializers import ClientsSerializer
from crm.serializers.admin.hikes_serializers import HikesIdAndNameSerializer
from crm.serializers.admin.statuses_serializers import StatusesSerializer
from rest_framework import serializers


class AllApplicationsSerializer(serializers.ModelSerializer):
    client = ClientsSerializer()
    hike = HikesIdAndNameSerializer()
    status = StatusesSerializer()

    class Meta:
        model = ApplicationsForHike
        fields = '__all__'
