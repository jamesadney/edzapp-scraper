from datetime import datetime

from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose, Identity
from scrapy.contrib_exp.djangoitem import DjangoItem
from django_edzapp.jobs.models import Job


def to_datetime(string):
    try:
        datetime_object = datetime.strptime(string, '%m/%d/%Y')
        out = unicode(datetime_object.date())
    except ValueError:
        out = None

    return out


class JobItemLoader(ItemLoader):
    default_input_processor = Identity()
    default_output_processor = Join()

    deadline_in = MapCompose(to_datetime)
    date_posted_in = MapCompose(to_datetime)


class JobItem(DjangoItem):
    django_model = Job
