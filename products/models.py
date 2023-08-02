from django.db import models

# Create your models here.
class Product(models.Model):
    sku = models.IntegerField(primary_key=True, null=False)
    product_name = models.CharField(max_length=200)
    availability = models.BooleanField(default=False)
    price = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    size = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/img')

    class Meta:
        db_table = 'product'

    # def __str__(self):
    #     return self.title + " - by: " + self.user.username