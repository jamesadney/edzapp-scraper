##############
Edzapp Scraper
##############

This is a little scraper I hacked together to pull job listings off of EdZapp to simplify the search process.

Installation
############

1. Install dependencies (Scrapy >= 0.14.4): ::
   
      pip install -r requirements.txt

2. Clone repository: ::
   
      git clone git://github.com/jamesadney/edzapp-scraper.git

Simple Usage
############

From inside the cloned edzapp-scraper folder: ::
   
   scrapy crawl edzapp -o jobs.csv -t csv

Customization
#############

Disable scraping job pages
--------------------------

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
