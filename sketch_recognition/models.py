from django.db import models

# Create your models here.

class Canvas(models.Model):
  user     = models.TextField()
  image      = models.ImageField(upload_to='canvas/')
  def __str__(self):
      return self.user
