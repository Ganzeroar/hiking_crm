from django.db import models


class Hikes(models.Model):
    hike_name = models.CharField(max_length=100)
    hike_description = models.CharField(max_length=2000)
