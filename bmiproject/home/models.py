from django.db import models

# Create your models here.

from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=10)
    weight = models.FloatField()
    height = models.FloatField()
    step = models.FloatField()
    burn = models.FloatField()
    eat = models.FloatField()
    sleep = models.FloatField()
    label = models.IntegerField(default=None)
    predict_label = models.IntegerField(default=None)
