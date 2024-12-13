from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels



DEFAULT_USER_ID = 1 

class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = jmodels.jDateField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID)

    def __str__(self):
        return f"{self.user.username}'s expense of {self.amount} on {self.date}"



class Income(models.Model):
    text = models.CharField(max_length=255)
    date = jmodels.jDateField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.username}'s income of {self.amount} on {self.date}"