from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
from django.utils.timezone import now
from PIL import Image

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    description = models.CharField(max_length = 200, default = "A new user")
    nickname = models.CharField(max_length = 32, default = "New User")
    profile_picture = models.ImageField(default = "default.png", upload_to = "profile_pictures")
    creationDate = models.DateField(default = now)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.profile_picture.path)

        if img.height >= 100 or img.width >= 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.profile_picture.path)
