from django.db import models

# Create your models here.
class contactus(models.Model):
    sno = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    content = models.TextField

