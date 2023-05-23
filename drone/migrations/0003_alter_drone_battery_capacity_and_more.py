# Generated by Django 4.1.3 on 2023-05-23 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0002_remove_drone_id_alter_drone_battery_capacity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='battery_capacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='drone',
            name='weight_limit',
            field=models.DecimalField(decimal_places=1, max_digits=4),
        ),
    ]
