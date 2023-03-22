from crm.api.client.all_hikes_view import AllHikes
from crm.api.client.specific_hike_view import SpecificHike
from crm.api.client.create_application import CreateApplication
from django.urls import path

urlpatterns = [
    path('client/hikings', AllHikes.as_view(), name='client-hikings'),
    path('client/hikings/<int:pk>', SpecificHike.as_view(), name='specific-hike'),
    path('client/create_appeal', CreateApplication.as_view(), name='create-appeal'),
]
