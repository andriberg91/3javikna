from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    logo = models.CharField(max_length=999, blank=True)
    year_of_start = models.DateTimeField()
    def __str__(self):
        return self.name
