from crm.models import Hikes
from rest_framework import serializers


class AdminHikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hikes
        fields = ['id', 'hike_name']


class AdminSpecificHikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hikes
        fields = '__all__'

    def update(self, instance, validated_data):
        hike_name = validated_data.get('hike_name')
        hike_description = validated_data.get('hike_description')

        Hikes.objects.filter(
            pk=instance.id,
        ).update(
            hike_name=hike_name,
            hike_description=hike_description,
        )

        return Hikes.objects.get(
            pk=instance.id,
        )


class AdminHikeIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='id')

    class Meta:
        model = Hikes
        fields = ['id']
