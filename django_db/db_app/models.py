from django.db import models

# Create your models here.
class Footballers(models.Model):
    name=models.CharField(max_length=40)
    position=models.CharField(max_length=50)
    age=models.IntegerField()