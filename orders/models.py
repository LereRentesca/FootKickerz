from accounts.models import User
from products.models import Product
from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.IntegerField(primary_key=True, null=False)
    order_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'order'