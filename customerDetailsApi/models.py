from django.db import models
from pandas.core.dtypes.dtypes import CategoricalDtypeType
from pandas.core.groupby.generic import generate_property

# Create your models here.

class Customers(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    email       = models.EmailField()
    gender      = models.CharField(max_length=30)
    company     = models.TextField()
    city        = models.TextField()
    title       = models.TextField()
    lon         = models.TextField(default="0", null=True)
    lat         = models.TextField(default="0", null=True)

    def __str__(self):
        return self.first_name + self.last_name