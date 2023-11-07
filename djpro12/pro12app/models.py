from django.db import models


# TABLE 만드는 곳
# Create your models here.

class Maker(models.Model):
    mname = models.CharField(max_length=20)
    mtel = models.CharField(max_length=30)
    maddr = models.CharField(max_length=50)
    
    # table 제조사에 브랜명이 보이는 이유가 된다.
    def __str__(self):
        return self.mname
    
class Product(models.Model):
    pname = models.CharField(max_length=20)
    pprice = models.IntegerField()
    pmaker_name = models.ForeignKey(Maker, on_delete=models.CASCADE) # FK는 Maker의 PK(id)를 참조