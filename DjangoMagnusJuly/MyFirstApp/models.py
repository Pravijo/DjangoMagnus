from django.db import models

# Create your models here.

class Employee(models.Model):
    empno = models.IntegerField()
    ename = models.CharField(max_length=40)
    sal = models.IntegerField()
    deptno = models.IntegerField()


class Pets(models.Model):
    petname = models.CharField(max_length=50)
    petcolor = models.CharField(max_length=30)
    petage = models.IntegerField()


class Car(models.Model):
    Brand = models.CharField(max_length=200)
    CModel = models.CharField(max_length=200)

    def __str__(self):
        return self.CModel