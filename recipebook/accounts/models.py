from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    shortBio = models.CharField(max_length=1000, validators=[MinLengthValidator(255)])
    
    def __str__(self):
        return self.name
