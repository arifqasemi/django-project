from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField('email', max_length=30)
    password = models.CharField('password',max_length=256,default='')
    image = models.FileField(upload_to='uploads',default='default.jpg')
