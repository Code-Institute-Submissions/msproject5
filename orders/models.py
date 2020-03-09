from django.db import models
from products.models import Product
from users.models import Profile

# Create your models here.
class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, related_name="orders", null=True, blank=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return f'{self.id}-{self.date}-{self.first_name}-{self.last_name}'


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(blank=False)
    def __str__(self):
        return f'{self.quantity} {self.product_name} @ {self.product_price}'
