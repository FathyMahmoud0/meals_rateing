from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Meal(models.Model):
    
    title = models.CharField(max_length=300)
    discription = models.CharField(max_length=360)
    
    def __str__(self):
        return self.title
    
    
class Rate(models.Model):
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField()
