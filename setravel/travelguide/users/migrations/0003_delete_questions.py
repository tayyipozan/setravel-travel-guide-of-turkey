# Generated by Django 3.2.6 on 2022-01-18 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_questions_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Questions',
        ),
    ]
