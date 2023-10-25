from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_carer = models.BooleanField(default=False)

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return self.username
