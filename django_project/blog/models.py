from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    position = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    fullname = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname.username

    #def get_absolute_url(self):
        #return reverse('post-detail', kwargs={'pk': self.pk})