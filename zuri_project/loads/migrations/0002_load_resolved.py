# Generated by Django 4.0.6 on 2022-07-26 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='load',
            name='resolved',
            field=models.BooleanField(default=False),
        ),
    ]
