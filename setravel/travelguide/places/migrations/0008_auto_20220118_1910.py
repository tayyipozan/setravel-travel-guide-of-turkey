# Generated by Django 3.2.6 on 2022-01-18 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20220114_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='score',
        ),
        migrations.RemoveField(
            model_name='place',
            name='created_date',
        ),
        migrations.AddField(
            model_name='comments',
            name='rating',
            field=models.IntegerField(default=None, verbose_name='rating'),
        ),
        migrations.AlterField(
            model_name='placedetail',
            name='category',
            field=models.CharField(default=None, max_length=50, verbose_name='Category_name'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
