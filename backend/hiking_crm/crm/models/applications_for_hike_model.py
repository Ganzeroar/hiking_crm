from django.db import models

from .clients_model import Clients
from .hikes_model import Hikes
from .statuses_model import Statuses


class ApplicationsForHike(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    hike = models.ForeignKey(Hikes, on_delete=models.CASCADE)
    status = models.ForeignKey(Statuses, on_delete=models.CASCADE)
    date_of_creation = models.DateTimeField(auto_now_add=True)
