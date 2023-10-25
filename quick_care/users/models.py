from django.db import models
from django.contrib.auth.models import AbstractUser



USER_STATUS = (
    ('unapproved', 'Unapproved'),
    ('approved', 'Approved')
)



class User(AbstractUser):
    is_carer = models.BooleanField(default=False)

    email = models.EmailField(unique=True)
    user_status = models.CharField(max_length=20, choices=USER_STATUS, default='unapproved')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return self.username
