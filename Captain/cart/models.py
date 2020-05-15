from django.db import models
from django.contrib.auth.models import User

from console.models import Console


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Console, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(CartItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username