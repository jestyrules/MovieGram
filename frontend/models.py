from django.db import models


# Create your models here.
class Registerdb(models.Model):
    Username = models.CharField(max_length=50, null=True, blank=True, unique=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)


class Cartdb(models.Model):
    MovieName = models.CharField(max_length=50, null=True, blank=True, unique=True)
    Language = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Category = models.CharField(max_length=50, null=True, blank=True)


class Checkoutdb(models.Model):
    Username = models.CharField(max_length=50, null=True, blank=True)
    Email = models.EmailField(max_length=50, null=True, blank=True)
    Contact = models.IntegerField(null=True, blank=True)
    Place = models.CharField(max_length=50, null=True, blank=True)
