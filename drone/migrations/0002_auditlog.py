# Generated by Django 4.1.3 on 2023-05-25 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battery_capacity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('drone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drone_details', to='drone.drone')),
            ],
        ),
    ]
