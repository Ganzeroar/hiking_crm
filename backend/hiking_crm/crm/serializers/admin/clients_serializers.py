from crm.models import Clients
from rest_framework.serializers import ModelSerializer


class ClientsSerializer(ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'
