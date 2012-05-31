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
DOWNLOAD_DELAY = 3

ROLE = constants.ROLES['TEACHER/CLASSIFIED']

try:
    from local_settings import *
except ImportError:
    pass
