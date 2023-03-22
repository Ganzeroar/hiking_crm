from crm.models import Hikes
from rest_framework import serializers


class HikesIdAndNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hikes
        fields = ['id', 'hike_name']
