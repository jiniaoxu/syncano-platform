# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 13:14
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0015_auto_20151116_1124'),
    ]

    operations = [
        migrations.RunSQL(
"""
CREATE INDEX admins_admin_trgm_email ON admins_admin
USING GIN (email gin_trgm_ops);
"""
        )
    ]
