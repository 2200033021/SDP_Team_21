from django.db import models


class vegitables(models.Model):
    vname = models.CharField(max_length=30)
    vprice = models.IntegerField(default=0)
    vinfo = models.TextField()
    vamm = models.CharField(max_length=30,null=True)
    vimg= models.ImageField(upload_to='static/imagesv/')




class grocrey(models.Model):
    gname = models.CharField(max_length=30)
    gprice = models.IntegerField(default=0)
    ginfo = models.TextField()
    gamm = models.CharField(max_length=30,null=True)
    gimg= models.ImageField(upload_to='static/imagesg/')
# Create your models here.

class Platform(models.Model):
    name = models.CharField(max_length=50)

class VegetablePlatform(models.Model):
    vegetable = models.ForeignKey(vegitables, on_delete=models.CASCADE, related_name='platforms')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField(blank=True)

class GroceryPlatform(models.Model):
    grocery = models.ForeignKey(grocrey, on_delete=models.CASCADE, related_name='platforms')
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.URLField(blank=True)
