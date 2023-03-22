from crm.models import ApplicationsForHike
from rest_framework import serializers


class ApplicationsForHikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationsForHike
        fields = '__all__'
