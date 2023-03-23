from crm.models import ApplicationsForHike
from rest_framework.serializers import ModelSerializer


class ApplicationsForHikeSerializer(ModelSerializer):
    class Meta:
        model = ApplicationsForHike
        fields = '__all__'
