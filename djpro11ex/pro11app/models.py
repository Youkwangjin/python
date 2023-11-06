from django.db import models

# Create your models here.

class Family(models.Model):
    # ('id', 'name', 'age', 'tel', 'gen')
    name = models.CharField(max_length = 100)
    age = models.IntegerField()
    tel = models.TextField()
    gen = models.CharField(max_length = 10)
    
