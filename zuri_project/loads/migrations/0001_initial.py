# Generated by Django 4.0.6 on 2022-07-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Load',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('load_number', models.CharField(max_length=50)),
                ('driver_assigned_to', models.CharField(max_length=50)),
                ('pickup_date', models.DateField(blank=True)),
                ('pickup_location', models.CharField(max_length=50)),
                ('dropoff_location', models.CharField(max_length=50)),
            ],
        ),
    ]
