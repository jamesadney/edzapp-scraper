from django.contrib import admin
from jobs.models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'position')

admin.site.register(Job, JobAdmin)