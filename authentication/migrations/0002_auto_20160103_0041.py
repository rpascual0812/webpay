# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='account',
            name='employeeid',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
    ]
