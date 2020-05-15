from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class SearchHistory(models.Model):
    search_word = models.CharField(max_length=225)
    time_stamp = models.DateTimeField()
    user = models.OneToOneField(User, on_delete='SET NULL', blank=True)
    def __str__(self):
        return self.search_word