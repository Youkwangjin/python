from django.db import models

# Create your models here.

class Article(models.Model): # 스프링에서 Entity라고 생각하자
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    pub_date = models.DateTimeField()
    
    