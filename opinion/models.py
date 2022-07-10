from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.contrib.auth.models import User
# User = settings.AUTH_USER_MODEL

class Drop(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return self.title
        
class Vote(models.Model):
    voter = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Drop,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'@{self.voter} voted {self.post}'
    
    