from django.db import models

# Create your models here.
class animals(models.Model):
    name=models.CharField(max_length=20)
    photo_bg=models.ImageField()
    description=models.TextField()