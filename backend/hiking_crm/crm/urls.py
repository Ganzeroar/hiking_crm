from crm.api.client.all_hikes_view import AllHikes
from crm.api.client.specific_hike_view import SpecificHike
from crm.api.client.create_application import CreateApplication
from crm.api.admin.all_applications import AllApplications
from crm.api.admin.update_application import UpdateApplication
from crm.api.admin.admin_all_hikes import AdminAllHikes
from django.urls import path

urlpatterns = [
    path('client/hikings', AllHikes.as_view(), name='client-hikings'),
    path('client/hikings/<int:pk>', SpecificHike.as_view(), name='specific-hike'),
    path('client/create_application', CreateApplication.as_view(), name='create-application'),

    path('admin/applications', AllApplications.as_view(), name='applications'),
    path('admin/applications/<int:pk>', UpdateApplication.as_view(), name='update-application'),
    path('admin/hikings', AdminAllHikes.as_view(), name='admin-hikes'),
]
