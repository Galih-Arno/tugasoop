from django.db import models

# Create your models here.
class Buku(models.Model):
    bookName = models.CharField(max_length=60)
    author = models.CharField(max_length=30)
    year = models.CharField(max_length=4)
    publisher = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    