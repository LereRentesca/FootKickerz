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

    def __str__(self):
        return f"""
        SKU: {self.sku}
        Product Name: {self.product_name}
        Availability: {self.availability}
        Price: {self.price}
        Description: {self.description}
        Size: {self.size}
        Image: {self.image}
    """

class Sport(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name