from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    email = models.EmailField(default="null")
    address = models.TextField(max_length=200)
    file = models.FileField()

