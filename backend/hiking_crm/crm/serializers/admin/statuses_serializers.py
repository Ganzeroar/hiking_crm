from crm.models import Statuses
from rest_framework.serializers import ModelSerializer, IntegerField


class StatusesSerializer(ModelSerializer):
    id = IntegerField(label='id')

    class Meta:
        model = Statuses
        fields = '__all__'
