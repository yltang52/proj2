from django.db import models
from account.models import User


class UserProfile2(models.Model):
    user = models.OneToOneField(User, related_name='userProfile2', on_delete=models.CASCADE)
    age = models.IntegerField()
