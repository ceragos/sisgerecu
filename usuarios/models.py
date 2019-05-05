from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    class Meta:
        unique_together = ('email',)

    def save(self, *args, **kwargs):
        return super(User, self).save(*args, **kwargs)