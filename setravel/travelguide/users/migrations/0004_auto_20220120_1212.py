# Generated by Django 3.2.6 on 2022-01-20 09:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_delete_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favplaces',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created Date'),
        ),
        migrations.CreateModel(
            name='UserResetPassInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('resquestion', models.CharField(max_length=100, verbose_name='resquestion')),
                ('resanswer', models.CharField(max_length=100, verbose_name='resanswer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
