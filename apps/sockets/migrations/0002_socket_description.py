# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-18 11:48
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sockets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socket',
            name='description',
            field=models.TextField(blank=True, max_length=256),
        ),
    ]