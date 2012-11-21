##############
Edzapp Scraper
##############

This is a little scraper I hacked together to pull job listings off of 
EdZapp to simplify the search process.  It isn't beautiful, but
hopefully it can be of some use to you!

Installation
############

1. Clone repository: ::
   
      git clone git://github.com/jamesadney/edzapp-scraper.git

2. Install dependencies (Scrapy >= 0.14.4): ::
   
      pip install -r requirements.txt

Simple Usage
############

From inside the cloned edzapp-scraper folder: ::
   
   scrapy crawl edzapp -o jobs.csv -t csv

Django Site
###########

I'm working on a Django frontend for the scraped data.  Currently, all it does
is store the scraped data in a database.

Setting up the Django project
-----------------------------

Generate a ``SECRET_KEY``
'''''''''''''''''''''''''

::

   >>> import os
   >>> os.urandom(24)
   '\xf3!\xd5\x8d\x07\x98\xa2\x0b\xf4\xc0Y]$\x11\x8aJ\xb3\x8fk\'\xa4"\xe9P'
   >>> # Of course, don't use this key!
    

Add the key to ``./edzapp/django_edzapp/django_edzapp/settings.py``.

Initialize the database
'''''''''''''''''''''''

From ``./edzapp/django_edzapp/`` run: ::

   python manage.py syncdb

Enable the ``DjangoJobPipeline``
''''''''''''''''''''''''''''''''

Uncomment ``'edzapp.pipelines.DjangoJobPipeline',`` in ``settings.py``. ::

   ITEM_PIPELINES = [
   #    'edzapp.pipelines.DjangoJobPipeline',
   ]


Customization
#############

Disable scraping job pages
--------------------------

**Disabling this will probably break the Django site**

By default, the scraper opens the link for each job to pull information from
the job's page.  This significantly increases the amount of time required to
scrape the site.  

If you don't need the extra information, open ``settings.py`` and change ::

   PARSE_JOB_PAGES = True

to ::

   PARSE_JOB_PAGES = False

Change the job "role"
---------------------

In order to minimize the number of pages scraped, the spider tells EdZapp to
only show positions labeled as "TEACHER/CLASSIFIED".  Other available search
options are:

    - STUDENT_SUPPORT_SERVICES
    - ADMINISTRATOR
    - INSTRUCTIONAL_SUPPORT
    - NON-INSTRUCTIONAL_SUPPORT
    - PROFESSIONAL/EXECUTIVE
    - EXTRACURRICULAR
    
To change this setting, open ``settings.py`` and use the role as listed above
as the keyword on this line instead of ``'TEACHER/CLASSIFIED'``. ::

   ROLE = constants.ROLES['TEACHER/CLASSIFIED']