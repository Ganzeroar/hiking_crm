from crm.models import ApplicationsForHike
from crm.models.clients_model import Clients
from crm.models.hikes_model import Hikes
from crm.models.statuses_model import Statuses
from crm.serializers.client.clients_serializers import ClientsSerializer
from crm.serializers.client.hikes_serializers import HikeIdSerializer
from rest_framework import serializers


class ApplicationSerializer(serializers.ModelSerializer):
    client = ClientsSerializer()
    hike = HikeIdSerializer()

    class Meta:
        model = ApplicationsForHike
        fields = ['client', 'hike']

    def create(self, validated_data):
        hike = Hikes.objects.get(pk=validated_data.get('hike').get('id'))

        client_data = validated_data.pop('client')
        client, _ = Clients.objects.get_or_create(**client_data)

        status = Statuses.objects.get(pk=1)

        return ApplicationsForHike.objects.create(
            client=client,
            hike=hike,
            status=status,
        )
