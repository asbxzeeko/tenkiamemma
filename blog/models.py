from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=140)
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    
    thumb = models.TextField()
    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    
    def __str__(self):
        return self.title
        
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=140)
    email = models.CharField(max_length=1024)
    text = models.TextField()
    
    created_date = models.DateTimeField(blank=True, null=True)
    
    def post_comment(self):
        self.created_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.text
        
