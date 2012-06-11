from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    job_id = models.IntegerField(primary_key=True)
    user = models.ManyToManyField(User)
    position = models.CharField(max_length=200, null=True, blank=True)
    url = models.URLField()
    organization = models.CharField(max_length=200, null=True, blank=True)
    school_name = models.TextField(null=True, blank=True)
    job_type = models.CharField(max_length=200, null=True, blank=True)
    salary = models.CharField(max_length=200, null=True, blank=True)
    is_external = models.CharField(max_length=200, null=True, blank=True)
    date_posted = models.DateField(null=True, blank=True)
    deadline = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    application_method = models.TextField(null=True, blank=True)
    grade_levels = models.CharField(max_length=400, null=True, blank=True)
    subject_areas = models.TextField(null=True, blank=True)
    employer_website = models.URLField(null=True, blank=True)
    local_contact = models.TextField(null=True, blank=True)
    community_description = models.TextField(null=True, blank=True)
