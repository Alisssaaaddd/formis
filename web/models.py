from django.db import models
from django.contrib.auth.models import User

DEFAULT_USER_ID = 1  # Ensure this matches the default user's ID

class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=DEFAULT_USER_ID)

    def __str__(self):
        return f"{self.user.username}'s expense of {self.amount} on {self.date}"
