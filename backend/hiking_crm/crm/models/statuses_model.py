from django.db import models


class Statuses(models.Model):
    status_name = models.CharField(max_length=30)
