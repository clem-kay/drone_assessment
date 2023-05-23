# Generated by Django 4.1.3 on 2023-05-23 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drone',
            name='id',
        ),
        migrations.AlterField(
            model_name='drone',
            name='battery_capacity',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='drone',
            name='serial_number',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='drone',
            name='weight_limit',
            field=models.CharField(max_length=5),
        ),
    ]
