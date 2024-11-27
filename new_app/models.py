from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_seller=models.BooleanField(default=False)
    is_coustmer=models.BooleanField(default=False)

class seller(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="seller")
    Name=models.CharField(max_length=20)
    Age = models.CharField(max_length=3)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=30)


class coustmer(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="coustmer")
    Name=models.CharField(max_length=20)
    Age = models.CharField(max_length=3)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=30)

class blog(models.Model):
    sellerName = models.ForeignKey('seller', on_delete=models.CASCADE)
    title=models.CharField(max_length=20)
    content=models.TextField()
    author=models.CharField(max_length=20)
    date=models.DateField()
    document = models.FileField(upload_to='documents/')