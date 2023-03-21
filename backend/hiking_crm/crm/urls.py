from crm.api.client.all_hikes_view import AllHikes
from django.urls import path

urlpatterns = [
    path('client/hikings', AllHikes.as_view(), name='client-hikings'),
]
