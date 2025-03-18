from django.db import models
from django.contrib.auth.models import User

# Post model
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

# Extending a user using one to one link to accomodate extra fields as profile_picture and bio
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_images/', blank=True, null=True)
    bio = models.TextField()
    
    def __str__(self):
        return self.user.username
    
    
