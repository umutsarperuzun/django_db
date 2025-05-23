from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.
class Footballers(models.Model):
    name=models.CharField(max_length=40)
    position=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(150)])
    salary=models.IntegerField(default=0,validators=[MinValueValidator(0)])
    
    def __str__(self):
        return f"Name: {self.name}, Position: {self.position} , Age: {self.age} , Salary: {self.salary}"