from django.db import models

# Create your models here.


# Create your models here.
class Lunbo(models.Model):
    title = models.CharField(max_length=20)
    pic = models.ImageField(upload_to="img")
    times = models.CharField(max_length=20)
    status = models.SmallIntegerField()


class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    times = models.CharField(max_length=20)
    status = models.SmallIntegerField()
    address = models.CharField(max_length=20)