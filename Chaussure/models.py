from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.utils import timezone 

class Chaussure(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField(default=' ')
    img = models.ImageField(upload_to='post_img/', default="post_img/default.png")
    created_at = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default =True)
    def __str__(self):
        return self.nom
