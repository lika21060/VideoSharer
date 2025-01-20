from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/profile_pics/', default='uploads/profile_pics/default.jpg', blank=True, null=True)

    def __str__(self):
        return self.user.username
