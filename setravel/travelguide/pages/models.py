from django.db import models

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    contactname = models.CharField(max_length=100, verbose_name='name')
    contactemail = models.CharField(max_length=100, verbose_name='email')
    contacttext = models.CharField(max_length=100, verbose_name='text')