# Generated by Django 4.0.6 on 2022-07-26 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0007_driver_citizenship_alter_driver_certification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='phone',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
