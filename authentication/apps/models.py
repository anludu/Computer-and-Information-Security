from django.db import models
from django.contrib.auth.models import User


class Application(models.Model):
    name = models.CharField(max_length=200)
    secret_password = models.CharField(max_length=12)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
