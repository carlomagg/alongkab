# Generated by Django 3.2.2 on 2021-05-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_alter_drivers_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drivers',
            name='address',
            field=models.CharField(default=None, max_length=60),
        ),
    ]