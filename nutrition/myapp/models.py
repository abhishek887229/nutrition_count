from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class food(models.Model):

    name=models.CharField(max_length=250)
    carbs=models.FloatField()
    protien=models.FloatField()
    fat=models.FloatField()
    calories=models.IntegerField()

    def __str__(self):
        return self.name



class Consumed(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    consumed=models.ForeignKey(food,on_delete=models.CASCADE)

    def __str__(self):
        x=str(self.consumed)
        return x

class goal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    daily_goal=models.IntegerField()

    def __str__(self):
        y=str(self.user)+"|"+str(self.date)+"|"+str(self.daily_goal)
        return y

