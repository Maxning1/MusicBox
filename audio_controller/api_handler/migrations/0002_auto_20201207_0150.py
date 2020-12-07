# Generated by Django 3.1.3 on 2020-12-07 01:50

import api_handler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_handler', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api_handler.models.generate_unique_code, max_length=8, unique=True),
        ),
    ]