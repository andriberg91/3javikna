from django.db import models

from manufacturer.models import Manufacturer


class ConsoleType(models.Model):
    name = models.CharField(max_length=255)

class Console(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2999, blank=True)
    type = models.ForeignKey(ConsoleType, on_delete=models.CASCADE)
    price = models.FloatField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

class ConsoleImage(models.Model):
    image = models.CharField(max_length=999)
    console = models.ForeignKey(Console, on_delete=models.CASCADE)