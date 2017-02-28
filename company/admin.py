from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Game, New, JobCategory, Job

admin.site.register(Game)
admin.site.register(New)
admin.site.register(JobCategory)
admin.site.register(Job)
