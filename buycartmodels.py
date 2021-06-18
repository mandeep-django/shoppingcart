from django.db import connections
from django.db import models

class buycartmodel(models.Model):
    userid = models.IntegerField()
    productid = models.IntegerField()
    qty = models.IntegerField()

    class Meta:
        db_table="cart"