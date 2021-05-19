from django.db import models

# Create your models here.

class blog(models.Model):
    title = models.TextField()
    descrition = models.TextField()
    price = models.TextField()
    summary = models.TextField(default = 'This is the summary')