from django.db import models

# Create your models here.


class Cuisine(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    imageURL = models.FileField(verbose_name="Image")


class CuisineType(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    imageURL = models.FileField(verbose_name="Image")
    description = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    tel = models.CharField(max_length=300)
    price = models.CharField(max_length=300)
