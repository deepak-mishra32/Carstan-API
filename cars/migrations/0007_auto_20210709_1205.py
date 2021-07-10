# Generated by Django 3.1.7 on 2021-07-09 06:35

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_auto_20210709_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardetail',
            name='Fuel_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('CNG', 'CNG'), ('Electric', 'Electric')], max_length=26, verbose_name='Fuel'),
        ),
    ]