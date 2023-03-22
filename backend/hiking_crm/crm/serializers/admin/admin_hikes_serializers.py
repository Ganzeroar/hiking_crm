from crm.models import Hikes
from rest_framework import serializers


class AdminHikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hikes
        fields = ['id', 'hike_name']


class AdminHikeIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='id')

    class Meta:
        model = Hikes
        fields = ['id']
