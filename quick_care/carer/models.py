from django.db import models
from users.models import User, Profile



GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)

IDENTITY_TYPE = (
    ('international passport', 'International Passport'),
    ('drivers licence', 'Drivers Licence'),
)


class ChildMinderKYC(models.Model):
    childminder = models.ForeignKey(User, on_delete=models.CASCADE, default='childminder')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, choices=GENDER, default='gender')
    photograph = models.ImageField(upload_to='minder_photo', default='photograph')
    date_registered = models.DateTimeField(auto_now_add=True)
    # Contact Details
    phone_number = models.CharField(max_length=14)
    city = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    house_number = models.CharField(max_length=10)
    number_of_occupants = models.IntegerField()
    # File Uploads
    identity_type = models.CharField(max_length=50, choices=IDENTITY_TYPE, default='identity_type')
    identity_image = models.ImageField(upload_to='carer_file', default='identity_image')
    child_minder_training = models.FileField(upload_to='carer_file')
    first_aid_training = models.FileField(upload_to='carer_file')
    dbs_criminal_record_check = models.FileField(upload_to='carer_file')
    child_care_register = models.BooleanField(default=False)
    home_risk_assessment = models.BooleanField(default=False)
    approved_mider = models.BooleanField(default=False)


    class Meta:
        verbose_name_plural = 'ChildMinderKYC'
        ordering = ['-date_registered']


    def __str__(self):
        return f'{self.childminder} - {self.first_name} {self.last_name}'







