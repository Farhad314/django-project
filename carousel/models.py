from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='carousel/')
    short_description = models.TextField()
    
class Slider(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to = 'carousel/')
    short_discription = models.TextField()
