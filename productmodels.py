from django.db import connections
from django.db import models

class productmodel(models.Model):
    categoryid = models.IntegerField()
    productname = models.CharField(max_length=100)
    productprice = models.CharField(max_length=100)
    productquantity = models.CharField(max_length=100)
    productimage = models.FileField()
    displayorder = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    special = models.IntegerField()
    class Meta:
        db_table="product"