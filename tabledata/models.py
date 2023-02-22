from django.db import models

class tabledata(models.Model):
    name=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=10)
    city=models.CharField(max_length=20)
    
class helps(models.Model):
    name=models.CharField(max_length=50)
    phone_no=models.CharField(max_length=10)
    mess=models.CharField(max_length=200)
    