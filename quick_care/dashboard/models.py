from django.db import models
from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_expired = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.name
        