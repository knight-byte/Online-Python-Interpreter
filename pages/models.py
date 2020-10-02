from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.urls import reverse


class BegPost(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    date_posted = models.DateTimeField(default=timezone.now)
    solution = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('beg-post-detail', kwargs={'pk': self.pk})


class AdvPost(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    date_posted = models.DateTimeField(default=timezone.now)
    solution = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('adv-post-detail', kwargs={'pk': self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    images = models.ImageField(
        default="default.png", upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.images.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.images.path)
