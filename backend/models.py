from django.db import models


# Create your models here.
class categorydb(models.Model):
    CategoryName = models.CharField(max_length=50, null=True, blank=True)


class languagedb(models.Model):
    Language = models.CharField(max_length=50, null=True, blank=True)


class productdb(models.Model):
    CategoryName = models.CharField(max_length=50, null=True, blank=True)
    Language = models.CharField(max_length=50, null=True, blank=True)
    MovieName = models.CharField(max_length=50, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Thumbnail = models.ImageField(upload_to="Thumb")
