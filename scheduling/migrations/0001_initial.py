# Generated by Django 4.1.5 on 2023-02-23 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.CharField(max_length=100)),
                ('uid', models.CharField(max_length=100)),
                ('schedule_type', models.CharField(max_length=100)),
                ('timezone', models.CharField(max_length=100)),
                ('schedule_id', models.CharField(max_length=100)),
                ('start_date', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule_day',
            fields=[
                ('schedule_day_id', models.AutoField(primary_key=True, serialize=False)),
                ('end_time', models.CharField(max_length=100)),
                ('start_time', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=100)),
                ('location_id', models.CharField(max_length=100)),
                ('schedule_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scheduling.schedule')),
            ],
        ),
    ]
