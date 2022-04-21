from django.db import models


# Createyour models here.
class db_1(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    des = models.TextField()




