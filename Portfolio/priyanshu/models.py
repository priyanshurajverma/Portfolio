from django.db import models
class Contact(models.Model):
    name=models.CharField(max_length=100)
    contact=models.CharField(max_length=122)
    email=models.CharField(max_length=150)


# Create your models here.

