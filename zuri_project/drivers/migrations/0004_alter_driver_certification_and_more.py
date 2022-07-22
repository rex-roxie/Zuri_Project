# Generated by Django 4.0.6 on 2022-07-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0003_driver_phone_alter_driver_driver_license_numbers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='certification',
            field=models.CharField(choices=[('hazard', 'Hazard'), ('tanker_endorsement', 'Tanker Endorsement'), ('both', 'Both Hazard and Tanker Endorsement'), ('neither', 'Neither')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_license_expiry_date',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='driver',
            name='driver_license_numbers',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='driver',
            name='email',
            field=models.EmailField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='driver',
            name='first_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='driver',
            name='last_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='driver',
            name='medical_card_expiry_date',
            field=models.DateField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='driver',
            name='medical_card_number',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='driver',
            name='phone',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='truck_number',
            field=models.CharField(default=None, max_length=50),
        ),
    ]