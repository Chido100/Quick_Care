from django.db import models
from users.models import User



AGE_GROUP = (
    ('select', 'Select'),
    ('newborn', 'Newborn'),
    ('toddler', 'Toddler'),
    ('pre-school', 'Pre-school'),
    ('primary_school', 'Primary school'),
    ('teenager(12+years)', 'Teenager(12+years)')
)

ADDITIONAL_CARE = (
    ('select', 'Select'),
    ('cooking', 'Cooking'),
    ('putting_kids_to_bed', 'Putting kids to bed'),
    ('homework_help', 'Homework help')
)


class CareSlot(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    number_of_kids = models.IntegerField()
    age_group = models.CharField(max_length=50, choices=AGE_GROUP, default='select')
    additional_care = models.CharField(max_length=50, choices=ADDITIONAL_CARE, default='select', blank=True, null=True)
    postcode = models.CharField(max_length=10)
    slot_date = models.DateTimeField(auto_now_add=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'CareSlots'

    def __str__(self):
        return f'{self.creator}'
    

    