from django.db import models
from django.contrib import auth
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return self.username

class Profile(models.Model):
    GENDER_CHOICES = (
        ('m', 'Male'),
        ('f', 'Female'),
        ('n', 'Perfer not to say')
    )
    user = models.OneToOneField(auth.models.User, on_delete=models.CASCADE)
    gender = models.CharField(max_length = 1, choices = GENDER_CHOICES,
                                                                blank = True)
    birth_date = models.DateField(null = True, blank = True)
    location = models.CharField(max_length = 50, blank = True)
    profile_pic  = models.ImageField(upload_to = 'profiles_images',blank = True)
    profile_pic_thumbnail = ImageSpecField(source='profile_pic',
                                      processors=[ResizeToFill(150, 150)],
                                      format='JPEG',
                                      options={'quality': 100})
    bio = models.TextField()

    def __str__(self):
        return self.user.username + '\'s Profile'
