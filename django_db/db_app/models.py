from django.db import models

# Create your models here.
class Footballers(models.Model):
    name=models.CharField(max_length=40)
    position=models.CharField(max_length=50)
    age=models.IntegerField()
    
    def __str__(self):
        return f"Name: {self.name}, Position: {self.position} , Age: {self.age}"