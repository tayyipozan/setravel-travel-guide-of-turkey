# Generated by Django 3.2.6 on 2022-02-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_contact_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='contactemail',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='text',
            new_name='contacttext',
        ),
        migrations.AddField(
            model_name='contact',
            name='contactname',
            field=models.CharField(default=0, max_length=100, verbose_name='name'),
            preserve_default=False,
        ),
    ]