from django.db import models
from places.models import Place
from django.contrib.auth.models import User


class FavPlaces(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    place = models.ForeignKey(Place, verbose_name='Place', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Created Date')

class UserResetPassInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name='User',on_delete=models.CASCADE)
    resquestion = models.CharField(max_length=100, verbose_name='resquestion')
    resanswer = models.CharField(max_length=100, verbose_name="resanswer")
