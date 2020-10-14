from django.db import models
#from django.contrib.auth.models import User
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='following', blank=True)
    bio = models.TextField(default='no bio...')
    profile_image = models.ImageField(upload_to='Profile_Image', 
                                        default='default.jpg', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def profiles_posts(self):
        return self.post_set.all()

    def __str__(self):
        return str(self.user.username)
    
    class Meta:
        ordering = ['-created',]