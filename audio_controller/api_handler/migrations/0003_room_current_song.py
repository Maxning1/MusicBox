# Generated by Django 3.1.3 on 2021-01-08 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_handler', '0002_auto_20201207_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='current_song',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
