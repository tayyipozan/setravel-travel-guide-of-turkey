# Generated by Django 3.2.6 on 2022-01-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20220112_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='name',
        ),
        migrations.AddField(
            model_name='placedetail',
            name='name',
            field=models.CharField(default=None, max_length=100, verbose_name='Place_Name'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=100, verbose_name='title'),
        ),
    ]
