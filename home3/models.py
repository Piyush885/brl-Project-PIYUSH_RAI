from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    #number=models.IntegerField()


