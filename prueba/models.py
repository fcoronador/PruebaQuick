from django.db import models
from django.contrib.auth.models import (User,AbstractBaseUser, BaseUserManager, PermissionsMixin)
from datetime import datetime, timedelta
from django.conf import settings

class clients(models.Model):
    document = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    contra = models.CharField(max_length=200, null=True)

class usuarios(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=30)
    contra = models.CharField(max_length=200)

#nuevo = clients(document=1013646919,
# first_name='Fredy',last_name='Coronado',
# email='fecoronado9@misena.edu.co',
# contra='password')
#nuevo.save()

class products(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    attribute4 = models.CharField(max_length=100)

class bills(models.Model):
    client_id = models.ForeignKey(clients, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=30)
    nit = models.IntegerField()
    code = models.IntegerField()

class bills_products(models.Model):
    bill_id = models.ForeignKey(bills, on_delete=models.CASCADE)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE)


