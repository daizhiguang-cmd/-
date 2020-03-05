from django.db import models

# Create your models here.


# Create your models here.
class Lunbo(models.Model):
    title = models.CharField(max_length=20)
    pic = models.ImageField(upload_to="img")
    times = models.CharField(max_length=20)
    status = models.SmallIntegerField()