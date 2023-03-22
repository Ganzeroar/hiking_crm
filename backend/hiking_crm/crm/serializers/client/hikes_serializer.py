from crm.models import Hikes
from rest_framework import serializers


class HikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hikes
        fields = '__all__'


class HikeIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='id')

    class Meta:
        model = Hikes
        fields = ['id']
