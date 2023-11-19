from django.db import models
from users.models import User



class Mail(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    header = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date_created']
        verbose_name_plural = 'Mails'

    
    def __str__(self):
        return self.header
