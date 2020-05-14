from django.db import models

from console.models import Console, ConsoleImage
# Create your models here.


class FrontConsole(models.Model):
    name = models.CharField