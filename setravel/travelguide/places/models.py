from django.db import models
from django.contrib.auth.models import User

class Place(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='title')
    cardimage = models.ImageField(
        upload_to='static/cardimages/', null=True, blank=True)
    is_published = models.BooleanField(default=True)

class PlaceDetail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Place_Name', default=None)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, verbose_name='Category_name', default=None)
    description = models.TextField(verbose_name='Place_Description')
    region = models.CharField(max_length=100, verbose_name='Place_region')
    city = models.TextField(verbose_name='Place_city')
    area = models.CharField(max_length=50, verbose_name='area', default=None)
    temp = models.CharField(max_length=50, verbose_name='temp', default=None)
    structure = models.CharField(max_length=50, verbose_name='structure', default=None)
    meal = models.CharField(max_length=50, verbose_name='meal', default=None)
    restaurant = models.CharField(max_length=50, verbose_name='restaurant', default=None)
    hotel = models.CharField(max_length=50, verbose_name='hotel', default=None)
    sea = models.CharField(max_length=50, verbose_name='sea', default=None)

class Images(models.Model):
    id = models.AutoField(primary_key=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='static/placeimages/', null=True, blank=True)
    is_poster = models.BooleanField(default=True)

class Comments(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    rating = models.IntegerField(verbose_name='rating', default=None)
    comment = models.CharField(max_length=420, verbose_name='comment')
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Adding_Time')