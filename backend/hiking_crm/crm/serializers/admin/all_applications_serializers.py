from crm.models import ApplicationsForHike
from crm.models.statuses_model import Statuses
from crm.serializers.admin.clients_serializers import ClientsSerializer
from crm.serializers.admin.hikes_serializers import HikesIdAndNameSerializer
from crm.serializers.admin.statuses_serializers import StatusesSerializer
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import APIException


class AllApplicationsSerializer(ModelSerializer):
    client = ClientsSerializer()
    hike = HikesIdAndNameSerializer()
    status = StatusesSerializer()

    class Meta:
        model = ApplicationsForHike
        fields = '__all__'

    def update(self, instance, validated_data):
        status_data = validated_data.get('status')
        if not Statuses.objects.filter(pk=status_data.get('id')).exists():
            raise APIException('Invalid status id')

        new_status = Statuses.objects.get(pk=status_data.get('id'))

        ApplicationsForHike.objects.filter(
            pk=instance.id,
        ).update(
            status=new_status,
        )

        return ApplicationsForHike.objects.get(pk=instance.id)
