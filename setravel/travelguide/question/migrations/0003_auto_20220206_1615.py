# Generated by Django 3.2.6 on 2022-02-06 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_auto_20220206_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer3',
            field=models.CharField(default=None, max_length=100, verbose_name='answer3'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer4',
            field=models.CharField(default=None, max_length=100, verbose_name='answer4'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer5',
            field=models.CharField(default=None, max_length=100, verbose_name='answer5'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer6',
            field=models.CharField(default=None, max_length=100, verbose_name='answer6'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer7',
            field=models.CharField(default=None, max_length=100, verbose_name='answer7'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer1',
            field=models.CharField(default=None, max_length=100, verbose_name='answer1'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer2',
            field=models.CharField(default=None, max_length=100, verbose_name='answer2'),
        ),
    ]