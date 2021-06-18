from django.db import connections
from django.db import models

class contactmodel(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        db_table = 'contactus'