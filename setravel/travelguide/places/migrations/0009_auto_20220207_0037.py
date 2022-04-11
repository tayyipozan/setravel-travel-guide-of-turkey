# Generated by Django 3.2.6 on 2022-02-06 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20220118_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='placedetail',
            name='area',
            field=models.CharField(default=None, max_length=50, verbose_name='area'),
        ),
        migrations.AddField(
            model_name='placedetail',
            name='hotel',
            field=models.CharField(default=None, max_length=50, verbose_name='hotel'),
        ),
        migrations.AddField(
            model_name='placedetail',
            name='meal',
            field=models.CharField(default=None, max_length=50, verbose_name='meal'),
        ),
        migrations.AddField(
            model_name='placedetail',
            name='restaurant',
            field=models.CharField(default=None, max_length=50, verbose_name='restaurant'),
        ),
        migrations.AddField(
            model_name='placedetail',
            name='sea',
            field=models.CharField(default=None, max_length=50, verbose_name='sea'),
        ),
        migrations.AddField(
            model_name='placedetail',
            name='structure',
            field=models.CharField(default=None, max_length=50, verbose_name='structure'),
        ),
        migrations.AddField(
            model_name='placedetail',
            name='temp',
            field=models.CharField(default=None, max_length=50, verbose_name='temp'),
        ),
    ]