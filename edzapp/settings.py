# Scrapy settings for edzapp project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
from edzapp import constants

BOT_NAME = 'edzapp'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['edzapp.spiders']
NEWSPIDER_MODULE = 'edzapp.spiders'
USER_AGENT = 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1'
ITEM_PIPELINES = [
    #    'edzapp.pipelines.DjangoJobPipeline',
]
DOWNLOAD_DELAY = 3

ROLE = constants.ROLES['TEACHER/CLASSIFIED']
PARSE_JOB_PAGES = True

import sys
import os

# Directory containing django project
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))

sys.path.insert(0, os.path.join(PROJECT_ROOT, 'django_edzapp'))

# Set the django settings environment variable
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_edzapp.settings'

try:
    from local_settings import *
except ImportError:
    pass
