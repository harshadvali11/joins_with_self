from django.db import models

# Create your models here.
from django.db import models

class Dept(models.Model):
    DEPTNO = models.IntegerField(primary_key=True)
    DNAME = models.CharField(max_length=255)
    LOC = models.CharField(max_length=255)

class Emp(models.Model):
    EMPNO = models.IntegerField(primary_key=True)
    ENAME = models.CharField(max_length=255)
    JOB = models.CharField(max_length=255)
    MGR = models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)
    HIREDATE = models.DateField()
    SAL = models.DecimalField(max_digits=10, decimal_places=2)
    COMM = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    DEPTNO = models.ForeignKey(Dept, on_delete=models.CASCADE)

class Salgrade(models.Model):
    GRADE = models.IntegerField(primary_key=True)
    LOSAL = models.DecimalField(max_digits=10, decimal_places=2)
    HISAL = models.DecimalField(max_digits=10, decimal_places=2)