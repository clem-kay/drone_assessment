# Generated by Django 4.1.3 on 2023-05-25 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='code',
            field=models.CharField(max_length=10),
        ),
    ]