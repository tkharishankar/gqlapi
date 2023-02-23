from django.contrib import admin

from scheduling.models import Schedule, Schedule_day

# Register your models here.
scheduleModels = [Schedule, Schedule_day]  # iterable list
admin.site.register(scheduleModels)
