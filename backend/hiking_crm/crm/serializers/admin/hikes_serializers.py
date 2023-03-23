from crm.models import Hikes
from rest_framework.serializers import ModelSerializer


class HikesIdAndNameSerializer(ModelSerializer):
    class Meta:
        model = Hikes
        fields = ['id', 'hike_name']
