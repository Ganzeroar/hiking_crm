from crm.models import Statuses
from rest_framework import serializers


class StatusesSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='id')

    class Meta:
        model = Statuses
        fields = '__all__'
