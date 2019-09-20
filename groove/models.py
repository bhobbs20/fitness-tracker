from django.db import models
from django.contrib.auth.models import User

class Groove(models.Model):
  groove = models.CharField(max_length=200)
  date = models.DateField()
  duration = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  
  def __str__(self):
    return self.name