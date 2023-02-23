from django.db import models


# Create your models here.
class Schedule(models.Model):
    schedule_id = models.AutoField(primary_key=True)
    end_date = models.CharField(max_length=100)
    uid = models.CharField(max_length=100)
    schedule_type = models.CharField(max_length=100)
    timezone = models.CharField(max_length=100)
    schedule_id = models.CharField(max_length=100)
    start_date = models.CharField(max_length=100)


class Schedule_day(models.Model):
    schedule_day_id = models.AutoField(primary_key=True)
    end_time = models.CharField(max_length=100)
    start_time = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    location_id = models.CharField(max_length=100)
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE)
