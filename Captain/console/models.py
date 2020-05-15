from django.db import models
from django.shortcuts import reverse

from manufacturer.models import Manufacturer


class ConsoleType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Console(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=999, blank=True)
    type = models.ForeignKey(ConsoleType, on_delete=models.CASCADE)
    price = models.FloatField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    detailed_description = models.CharField(max_length=3999, blank=True)
    def __str__(self):
        return self.name

    def get_add_to_cart_url(self):
        return reverse("core:console", kwargs={
            'id': self.id
        })



class ConsoleImage(models.Model):
    image = models.CharField(max_length=999)
    console = models.ForeignKey(Console, on_delete=models.CASCADE)
    def __str__(self):
        return self.image