from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.CharField()
    password = models.CharField()

    class Meta:
        db_table = 'user'