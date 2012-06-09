from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    user = models.ManyToManyField(User)
    position = models.CharField(max_length=200)
    url = models.URLField()
    job_id = models.IntegerField()
    organization = models.CharField(max_length=200)
    school_name = models.TextField()
    job_type = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    is_external = models.CharField(max_length=200)
    date_posted = models.DateField()
    deadline = models.DateField()
    description = models.TextField()
    application_method = models.TextField()
    grade_levels = models.CharField(max_length=400)
    subject_areas = models.TextField()
    employer_website = models.URLField()
    local_contact = models.TextField()
    community_description = models.TextField()
