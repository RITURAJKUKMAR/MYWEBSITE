from django.db import models

class User(models.Model):
    username=models.CharField(primary_key=True,max_length=20)
    password=models.CharField(null=False,max_length=20)
    name=models.CharField(null=False,max_length=30)
    classTh=models.IntegerField(max_length=4)
    email=models.EmailField(null=False,max_length=50)
    mobileNo=models.IntegerField(null=False,max_length=11)
    test_attempted=models.IntegerField(default=0)
    points=models.FloatField(default=0.0)


class Question(models.Model):
    qid=models.BigAutoField(primary_key=True,auto_created=True)
    que=models.TextField()
    classTh=models.IntegerField(max_length=4)
    a=models.CharField(max_length=255)
    b=models.CharField(max_length=255)
    c=models.CharField(max_length=255)
    d=models.CharField(max_length=255)
    ans=models.CharField(max_length=2)


class Result(models.Model):
    resultid=models.BigAutoField(primary_key=True,auto_created=True)
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    attempt=models.IntegerField()
    right=models.IntegerField()
    worng=models.IntegerField()
    points=models.FloatField()