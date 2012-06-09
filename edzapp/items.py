from scrapy.contrib_exp.djangoitem import DjangoItem
from django_edzapp.jobs.models import Job

class JobItem(DjangoItem):
    django_model = Job
