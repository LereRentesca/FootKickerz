from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    class Meta:
        db_table = 'user'